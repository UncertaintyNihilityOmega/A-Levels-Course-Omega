@chapter bio.meiosis
@title Meiosis and genetic variation
@level a2
@paper CAIE 9700 Paper 4
@time 4–5 hours
@summary Meiosis halves the chromosome number so that gametes are haploid and fertilisation restores the diploid number. You will learn haploid and diploid, homologous pairs, the eight stages of meiosis and what happens to the chromosomes, nuclear envelope, spindle and cell surface membrane, how to recognise each stage, and how crossing over, random orientation and random fertilisation make every individual genetically different.

:::why
You are not a copy of either parent, and you are not a copy of your brother or sister. The reason is meiosis, the special cell division that makes sperm and egg cells, followed by the chance meeting of one sperm with one egg. Meiosis also explains why the chromosome number stays the same from one generation to the next. Paper 4 asks you to draw and recognise the stages, to count chromosomes and chromatids at each one, and to explain in marking points how variation arises. This chapter is the base for all the genetics that follows.
:::

**Before you start**, you should know the structure of a chromosome and the stages of mitosis from [Chromosomes and the mitotic cell cycle](#bio.mitosis), and how DNA is copied from [Nucleic acids and DNA replication](#bio.dna).

:::try Warm-up
Q: A human cell has 46 chromosomes in G1. How many chromosomes and how many chromatids does it have in G2? (from [Chromosomes and the mitotic cell cycle](#bio.mitosis))
A: 46 chromosomes. After DNA replication each chromosome is made of two chromatids, so there are 92 chromatids.
Q: Why are the two daughter cells of mitosis genetically identical to the parent cell? (from [Chromosomes and the mitotic cell cycle](#bio.mitosis))
A: DNA replication makes an identical copy of every chromosome, as two sister chromatids. In anaphase the chromatids separate, so each daughter cell gets one copy of every chromosome.
Q: What name is given to a sequence of DNA bases that codes for one polypeptide? (from [Protein synthesis and gene mutation](#bio.synthesis))
A: A gene.
:::

## Haploid and diploid cells

Almost every cell in your body contains 46 chromosomes. You do not have 46 different chromosomes: you have **23 pairs**. In each pair, one chromosome came from your mother (in her egg) and one from your father (in his sperm).

:::def Homologous pair of chromosomes
Two chromosomes in a diploid cell that have the same structure (the same length and centromere position) and carry the same genes at the same loci. One of the pair is inherited from each parent.
:::

The word **locus** (plural loci) means the position of a gene on a chromosome. The two chromosomes of a homologous pair carry the same genes in the same order, so a gene has its locus at the same place on both. The genes are the same, but the **alleles** (the different forms of a gene) may differ. These words are defined fully in [Monohybrid inheritance](#bio.inheritance); for now, an allele is one version of a gene.

:::html
<figure class="fig small"><svg viewBox="0 0 330 236" role="img" aria-label="A homologous pair of chromosomes, one maternal and one paternal, the same length with the centromere in the same place. Both carry the same genes at the same loci: gene A with alleles A on the maternal and a on the paternal chromosome, gene B with allele B on both, and gene D with alleles D and d."><text class="tl" x="110" y="30" text-anchor="middle">maternal</text><text class="tl" x="190" y="30" text-anchor="middle">paternal</text><rect class="fm s-acc sw2" x="97" y="44" width="26" height="172" rx="13"/><rect class="fm s-acc sw2" x="177" y="44" width="26" height="172" rx="13"/><circle class="fi" cx="110" cy="118" r="5"/><circle class="fi" cx="190" cy="118" r="5"/><rect class="fa s-acc sw2" x="97" y="61" width="26" height="10"/><rect class="fa s-acc sw2" x="177" y="61" width="26" height="10"/><text class="tl" x="133" y="70">A</text><text class="tl" x="162" y="70">a</text><text class="tl" x="226" y="70">gene A locus</text><path class="ln-m thin" d="M222 66L206 66"/><rect class="fa s-acc sw2" x="97" y="145" width="26" height="10"/><rect class="fa s-acc sw2" x="177" y="145" width="26" height="10"/><text class="tl" x="133" y="154">B</text><text class="tl" x="162" y="154">B</text><text class="tl" x="226" y="154">gene B locus</text><path class="ln-m thin" d="M222 150L206 150"/><rect class="fa s-acc sw2" x="97" y="183" width="26" height="10"/><rect class="fa s-acc sw2" x="177" y="183" width="26" height="10"/><text class="tl" x="133" y="192">D</text><text class="tl" x="162" y="192">d</text><text class="tl" x="226" y="192">gene D locus</text><path class="ln-m thin" d="M222 188L206 188"/><text class="tl" x="8" y="122">centromere</text><path class="ln-m thin" d="M80 118L99 118"/></svg><figcaption>A homologous pair (a drawing; each chromosome is drawn before DNA replication, as a single chromatid). The two chromosomes carry the same genes at the same loci, but the alleles can differ: here gene A has alleles A and a, gene B has B on both, and gene D has D and d.</figcaption></figure>
:::

:::def Diploid (2n)
A cell with two complete sets of chromosomes, one set from each parent, so that its chromosomes are in homologous pairs. The diploid number is written 2n.
:::

:::def Haploid (n)
A cell with one complete set of chromosomes, with one chromosome of each homologous pair. The haploid number is written n.
:::

Human body cells (somatic cells) are diploid, with 2n = 46. Human gametes (sperm and egg cells) are haploid, with n = 23. Other species have other numbers, and the number says nothing about how complex an organism is.

| organism | diploid number (2n) | haploid number (n) |
|---|---|---|
| human | 46 | 23 |
| fruit fly | 8 | 4 |
| garden pea | 14 | 7 |
| maize | 20 | 10 |
| domestic dog | 78 | 39 |

:::warn Homologous chromosomes are not identical
A homologous pair has the same genes in the same order, but the alleles may differ: one chromosome may carry the allele for brown eyes and the other the allele for blue eyes. **Sister chromatids**, in contrast, are identical copies of one chromosome made by DNA replication. Do not mix up "homologous" (a maternal and a paternal chromosome) with "sister" (two copies of the same chromosome).
:::

## Why gametes must be haploid

:::def Meiosis
A form of nuclear division in which a diploid nucleus divides twice to form four genetically different haploid nuclei. It is also called reduction division, because the chromosome number is halved.
:::

Gametes fuse in fertilisation. If gametes were diploid, the zygote would have twice as many chromosomes as its parents, and each generation would double the number:

\[\begin{aligned} \text{parents: } 2n &= 46 \\ \text{zygote if gametes were diploid: } &= 46 + 46 = 92 \\ \text{next generation: } &= 92 + 92 = 184 \end{aligned}\]

Meiosis prevents this. It halves the number to n = 23 in the gametes, so that fertilisation (n + n) restores 2n = 46. The chromosome number stays the same from generation to generation.

In an animal, meiosis happens in the ovaries and testes, and the haploid cells it makes become gametes directly. In a flowering plant, meiosis happens in the anthers and ovules and makes haploid cells that develop into pollen grains and the embryo sac. Mitosis in those structures then makes the gametes themselves.

:::key Why meiosis is needed
- Fertilisation joins two haploid gametes to make a diploid zygote.
- Meiosis is a **reduction division** that halves the chromosome number (2n to n).
- So the diploid number stays the same in every generation.
- It also makes the gametes **genetically different** from each other, which you will see below.
:::

## The stages of meiosis

Before meiosis starts, the cell goes through interphase, including S phase, when each chromosome is copied. So at the start of meiosis each chromosome is made of **two sister chromatids** joined at a centromere, exactly as before mitosis (see [Chromosomes and the mitotic cell cycle](#bio.mitosis)).

Then the nucleus divides twice with no more DNA replication between the divisions:
- **Meiosis I** separates the **homologous chromosomes**. This is the reduction division: the chromosome number halves, from 2n to n.
- **Meiosis II** separates the **sister chromatids**. It looks like mitosis, but starts with haploid cells.

Each division has four stages, with the same names as in mitosis: prophase, metaphase, anaphase and telophase. The stages are called prophase I, metaphase I, anaphase I, telophase I, prophase II, metaphase II, anaphase II and telophase II. (Prophase I has sub-divisions, but you do not need their names.)

For each stage, describe what happens to four things: the **chromosomes**, the **nuclear envelope**, the **spindle** and the **cell surface membrane**. The drawings show an animal cell with 2n = 4: two longer chromosomes that form one pair, and two shorter chromosomes that form another.

### Meiosis I

:::html
<figure class="fig small"><svg viewBox="0 0 330 300" role="img" aria-label="Two stages of meiosis I in an animal cell with four chromosomes. Prophase I: homologous chromosomes pair up as bivalents with chiasmata, and the nuclear envelope breaks down. Metaphase I: the bivalents line up on the equator, each chromosome attached by its centromere to fibres from one pole."><path class="fp ln" d="M134 76L133.5 84.1L131.9 92L129.3 99.7L125.7 107L121.2 113.7L115.8 119.8L109.7 125.2L103 129.7L95.7 133.3L88 135.9L80.1 137.5L72 138L63.9 137.5L56 135.9L48.3 133.3L41 129.7L34.3 125.2L28.2 119.8L22.8 113.7L18.3 107L14.7 99.7L12.1 92L10.5 84.1L10 76L10.5 67.9L12.1 60L14.7 52.3L18.3 45L22.8 38.3L28.2 32.2L34.3 26.8L41 22.3L48.3 18.7L56 16.1L63.9 14.5L72 14L80.1 14.5L88 16.1L95.7 18.7L103 22.3L109.7 26.8L115.8 32.2L121.2 38.3L125.7 45L129.3 52.3L131.9 60L133.5 67.9Z"/><path class="ln-m thin dash" d="M106 76L105.7 80.4L104.8 84.8L103.4 89L101.4 93L99 96.7L96 100L92.7 103L89 105.4L85 107.4L80.8 108.8L76.4 109.7L72 110L67.6 109.7L63.2 108.8L59 107.4L55 105.4L51.3 103L48 100L45 96.7L42.6 93L40.6 89L39.2 84.8L38.3 80.4L38 76L38.3 71.6L39.2 67.2L40.6 63L42.6 59L45 55.3L48 52L51.3 49L55 46.6L59 44.6L63.2 43.2L67.6 42.3L72 42L76.4 42.3L80.8 43.2L85 44.6L89 46.6L92.7 49L96 52L99 55.3L101.4 59L103.4 63L104.8 67.2L105.7 71.6Z"/><path class="c1 sw3" d="M57.935 51.4362L60.7185 71.2415"/><path class="c1 sw3" d="M65.2046 53.2487L53.4489 69.429"/><circle class="fi" cx="59.3267" cy="61.3389" r="2.2"/><path class="c1 sw3" d="M79.2815 56.7585L82.065 76.5638"/><path class="c1 sw3" d="M86.5511 58.571L74.7954 74.7513"/><circle class="fi" cx="80.6733" cy="66.6611" r="2.2"/><path class="ln" d="M67 61L73 67"/><path class="ln" d="M67 67L73 61"/><path class="c2 sw3" d="M62.4121 85.4528L69.831 97.3255"/><path class="c2 sw3" d="M67.5769 84.5422L64.6662 98.2362"/><circle class="fi" cx="66.1215" cy="91.3892" r="2.2"/><path class="c2 sw3" d="M78.169 82.6745L85.5879 94.5472"/><path class="c2 sw3" d="M83.3338 81.7638L80.4231 95.4578"/><circle class="fi" cx="81.8785" cy="88.6108" r="2.2"/><path class="ln" d="M71 87L77 93"/><path class="ln" d="M71 93L77 87"/><rect class="fi" x="20" y="70" width="4" height="12"/><rect class="fi" x="16" y="74" width="12" height="4"/><rect class="fi" x="120" y="70" width="4" height="12"/><rect class="fi" x="116" y="74" width="12" height="4"/><text class="tl tb" x="152" y="24">1  Prophase I</text><text class="tl" x="152" y="50">homologous pairs join</text><text class="tl" x="152" y="64">up (bivalents)</text><path class="ln-m thin" d="M148 46L90 60"/><text class="tl" x="152" y="96">nuclear envelope</text><text class="tl" x="152" y="110">breaking down</text><path class="ln-m thin" d="M148 92L102 98"/><text class="tl" x="152" y="134">chiasma</text><path class="ln-m thin" d="M148 130L80 92"/><path class="fp ln" d="M134 226L133.5 234.1L131.9 242L129.3 249.7L125.7 257L121.2 263.7L115.8 269.8L109.7 275.2L103 279.7L95.7 283.3L88 285.9L80.1 287.5L72 288L63.9 287.5L56 285.9L48.3 283.3L41 279.7L34.3 275.2L28.2 269.8L22.8 263.7L18.3 257L14.7 249.7L12.1 242L10.5 234.1L10 226L10.5 217.9L12.1 210L14.7 202.3L18.3 195L22.8 188.3L28.2 182.2L34.3 176.8L41 172.3L48.3 168.7L56 166.1L63.9 164.5L72 164L80.1 164.5L88 166.1L95.7 168.7L103 172.3L109.7 176.8L115.8 182.2L121.2 188.3L125.7 195L129.3 202.3L131.9 210L133.5 217.9Z"/><path class="c1 sw3" d="M57.2539 200.728L64.7461 219.272"/><path class="c1 sw3" d="M64.7461 200.728L57.2539 219.272"/><circle class="fi" cx="61" cy="210" r="2.2"/><path class="c1 sw3" d="M79.2539 200.728L86.7461 219.272"/><path class="c1 sw3" d="M86.7461 200.728L79.2539 219.272"/><circle class="fi" cx="83" cy="210" r="2.2"/><path class="ln" d="M69 207L75 213"/><path class="ln" d="M69 213L75 207"/><path class="c2 sw3" d="M61.3778 235.51L66.6222 248.49"/><path class="c2 sw3" d="M66.6222 235.51L61.3778 248.49"/><circle class="fi" cx="64" cy="242" r="2.2"/><path class="c2 sw3" d="M77.3778 235.51L82.6222 248.49"/><path class="c2 sw3" d="M82.6222 235.51L77.3778 248.49"/><circle class="fi" cx="80" cy="242" r="2.2"/><path class="ln" d="M69 239L75 245"/><path class="ln" d="M69 245L75 239"/><path class="ln-m thin" d="M20 226L61 210"/><path class="ln-m thin" d="M124 226L83 210"/><path class="ln-m thin" d="M20 226L64 242"/><path class="ln-m thin" d="M124 226L80 242"/><rect class="fi" x="18" y="220" width="4" height="12"/><rect class="fi" x="14" y="224" width="12" height="4"/><rect class="fi" x="122" y="220" width="4" height="12"/><rect class="fi" x="118" y="224" width="12" height="4"/><text class="tl tb" x="152" y="174">2  Metaphase I</text><text class="tl" x="152" y="200">pairs line up on</text><text class="tl" x="152" y="214">the equator</text><path class="ln-m thin" d="M148 196L86 208"/><text class="tl" x="152" y="246">each chromosome has</text><text class="tl" x="152" y="260">fibres from one pole</text><path class="ln-m thin" d="M148 242L102 234"/></svg><figcaption>Prophase I and metaphase I (drawings of an animal cell, 2n = 4). Each chromosome has two chromatids. The two longer chromosomes are one homologous pair and the two shorter ones another.</figcaption></figure>
:::

**Prophase I**
- The chromosomes condense (coil up, shorten and thicken) and become visible. Each is two sister chromatids.
- **Homologous chromosomes pair up**, gene by gene along their whole length. Each pair is a **bivalent**.
- **Crossing over** happens: non-sister chromatids of the two homologues break and rejoin, swapping sections. The points where they remain joined can be seen as crossing points called **chiasmata** (singular chiasma).
- The nucleolus disappears and the nuclear envelope breaks down. In animal cells the centrioles move to the poles and the spindle starts to form.

**Metaphase I**
- The spindle is complete. The **bivalents line up on the equator**, with the two chromosomes of each pair on opposite sides of it.
- Each chromosome is attached by its centromere to spindle fibres from **one** pole only. The two homologues of a pair face opposite poles.
- Each bivalent lies either way round, independently of the others (random orientation, below).

:::html
<figure class="fig small"><svg viewBox="0 0 330 300" role="img" aria-label="Two stages of meiosis I. Anaphase I: whole chromosomes, each still made of two chromatids, are pulled from each pair to opposite poles. Telophase I: two cells, each with two chromosomes, one from each homologous pair."><path class="fp ln" d="M134 76L133.5 84.1L131.9 92L129.3 99.7L125.7 107L121.2 113.7L115.8 119.8L109.7 125.2L103 129.7L95.7 133.3L88 135.9L80.1 137.5L72 138L63.9 137.5L56 135.9L48.3 133.3L41 129.7L34.3 125.2L28.2 119.8L22.8 113.7L18.3 107L14.7 99.7L12.1 92L10.5 84.1L10 76L10.5 67.9L12.1 60L14.7 52.3L18.3 45L22.8 38.3L28.2 32.2L34.3 26.8L41 22.3L48.3 18.7L56 16.1L63.9 14.5L72 14L80.1 14.5L88 16.1L95.7 18.7L103 22.3L109.7 26.8L115.8 32.2L121.2 38.3L125.7 45L129.3 52.3L131.9 60L133.5 67.9Z"/><path class="c1 sw3" d="M35.951 64.4741L56.049 55.5259"/><path class="c1 sw3" d="M35.951 55.5259L56.049 64.4741"/><circle class="fi" cx="46" cy="60" r="2.2"/><path class="c2 sw3" d="M38.6916 95.2539L53.3084 88.7461"/><path class="c2 sw3" d="M38.6916 88.7461L53.3084 95.2539"/><circle class="fi" cx="46" cy="92" r="2.2"/><path class="c1 sw3" d="M87.951 64.4741L108.049 55.5259"/><path class="c1 sw3" d="M87.951 55.5259L108.049 64.4741"/><circle class="fi" cx="98" cy="60" r="2.2"/><path class="c2 sw3" d="M90.6916 95.2539L105.308 88.7461"/><path class="c2 sw3" d="M90.6916 88.7461L105.308 95.2539"/><circle class="fi" cx="98" cy="92" r="2.2"/><path class="ln-m thin" d="M20 76L49 60"/><path class="ln-m thin" d="M20 76L49 92"/><path class="ln-m thin" d="M124 76L95 60"/><path class="ln-m thin" d="M124 76L95 92"/><rect class="fi" x="18" y="70" width="4" height="12"/><rect class="fi" x="14" y="74" width="12" height="4"/><rect class="fi" x="122" y="70" width="4" height="12"/><rect class="fi" x="118" y="74" width="12" height="4"/><text class="tl tb" x="152" y="24">3  Anaphase I</text><text class="tl" x="152" y="50">homologous pairs</text><text class="tl" x="152" y="64">separate</text><path class="ln-m thin" d="M148 46L100 56"/><text class="tl" x="152" y="96">chromatids stay</text><text class="tl" x="152" y="110">joined</text><path class="ln-m thin" d="M148 92L102 90"/><text class="tl" x="152" y="134">fibres shorten</text><path class="ln-m thin" d="M148 130L116 78"/><path class="fp ln" d="M138 226L137.6 231.6L136.6 237.2L134.8 242.7L132.3 248L129.2 253L125.4 257.7L121 262.1L116.2 266.1L110.8 269.7L105 272.7L98.8 275L92.4 275.5L85.7 272.8L78.9 267.1L72 263.8L65.1 267.1L58.3 272.8L51.6 275.5L45.2 275L39 272.7L33.2 269.7L27.8 266.1L23 262.1L18.6 257.7L14.8 253L11.7 248L9.2 242.7L7.4 237.2L6.4 231.6L6 226L6.4 220.4L7.4 214.8L9.2 209.3L11.7 204L14.8 199L18.6 194.3L23 189.9L27.8 185.9L33.2 182.3L39 179.3L45.2 177L51.6 176.5L58.3 179.2L65.1 184.9L72 188.2L78.9 184.9L85.7 179.2L92.4 176.5L98.8 177L105 179.3L110.8 182.3L116.2 185.9L121 189.9L125.4 194.3L129.2 199L132.3 204L134.8 209.3L136.6 214.8L137.6 220.4Z"/><path class="ln" d="M57 226L56.8 228.5L56.4 230.9L55.6 233.3L54.5 235.5L53.1 237.6L51.4 239.4L49.6 241.1L47.5 242.5L45.3 243.6L42.9 244.4L40.5 244.8L38 245L35.5 244.8L33.1 244.4L30.7 243.6L28.5 242.5L26.4 241.1L24.6 239.4L22.9 237.6L21.5 235.5L20.4 233.3L19.6 230.9L19.2 228.5L19 226L19.2 223.5L19.6 221.1L20.4 218.7L21.5 216.5L22.9 214.4L24.6 212.6L26.4 210.9L28.5 209.5L30.7 208.4L33.1 207.6L35.5 207.2L38 207L40.5 207.2L42.9 207.6L45.3 208.4L47.5 209.5L49.6 210.9L51.4 212.6L53.1 214.4L54.5 216.5L55.6 218.7L56.4 221.1L56.8 223.5Z"/><path class="c1 sw3" d="M31.6052 222.847L44.3948 217.153"/><path class="c1 sw3" d="M31.6052 217.153L44.3948 222.847"/><circle class="fi" cx="38" cy="220" r="2.2"/><path class="c2 sw3" d="M33.4323 235.034L42.5677 230.966"/><path class="c2 sw3" d="M33.4323 230.966L42.5677 235.034"/><circle class="fi" cx="38" cy="233" r="2.2"/><path class="ln" d="M125 226L124.8 228.5L124.4 230.9L123.6 233.3L122.5 235.5L121.1 237.6L119.4 239.4L117.6 241.1L115.5 242.5L113.3 243.6L110.9 244.4L108.5 244.8L106 245L103.5 244.8L101.1 244.4L98.7 243.6L96.5 242.5L94.4 241.1L92.6 239.4L90.9 237.6L89.5 235.5L88.4 233.3L87.6 230.9L87.2 228.5L87 226L87.2 223.5L87.6 221.1L88.4 218.7L89.5 216.5L90.9 214.4L92.6 212.6L94.4 210.9L96.5 209.5L98.7 208.4L101.1 207.6L103.5 207.2L106 207L108.5 207.2L110.9 207.6L113.3 208.4L115.5 209.5L117.6 210.9L119.4 212.6L121.1 214.4L122.5 216.5L123.6 218.7L124.4 221.1L124.8 223.5Z"/><path class="c1 sw3" d="M99.6052 222.847L112.395 217.153"/><path class="c1 sw3" d="M99.6052 217.153L112.395 222.847"/><circle class="fi" cx="106" cy="220" r="2.2"/><path class="c2 sw3" d="M101.432 235.034L110.568 230.966"/><path class="c2 sw3" d="M101.432 230.966L110.568 235.034"/><circle class="fi" cx="106" cy="233" r="2.2"/><text class="tl tb" x="152" y="174">4  Telophase I</text><text class="tl" x="152" y="200">two cells; each has</text><text class="tl" x="152" y="214">one of each pair</text><path class="ln-m thin" d="M148 196L118 218"/><text class="tl" x="152" y="246">chromosomes still</text><text class="tl" x="152" y="260">have 2 chromatids</text><path class="ln-m thin" d="M148 242L114 234"/><text class="tl" x="152" y="284">cell starts to divide</text><path class="ln-m thin" d="M148 280L74 256"/></svg><figcaption>Anaphase I and telophase I. The homologues of each pair separate, so each new cell has only two chromosomes: the number has halved.</figcaption></figure>
:::

**Anaphase I**
- The spindle fibres shorten and pull the **homologous chromosomes** of each pair to opposite poles, centromere first.
- The centromeres **do not divide**, so each chromosome still has two chromatids.
- The chiasmata slide apart as the pairs separate.

**Telophase I**
- The chromosomes reach the poles. In many cells they uncoil and a nuclear envelope re-forms around each group.
- The cell surface membrane pinches in (in an animal cell; a new cell wall forms across a plant cell) and the cytoplasm divides: **two haploid cells**.
- Each new cell has half as many chromosomes as the parent cell, one from each homologous pair, each still made of two chromatids.

There is a short gap before meiosis II, and **no DNA replication** in it.

### Meiosis II

:::html
<figure class="fig small"><svg viewBox="0 0 330 300" role="img" aria-label="Two stages of meiosis II in one of the two cells. Prophase II: a new spindle forms and the nuclear envelope breaks down. Metaphase II: the two chromosomes line up singly on the equator, attached to fibres from both poles."><path class="fp ln" d="M134 76L133.5 84.1L131.9 92L129.3 99.7L125.7 107L121.2 113.7L115.8 119.8L109.7 125.2L103 129.7L95.7 133.3L88 135.9L80.1 137.5L72 138L63.9 137.5L56 135.9L48.3 133.3L41 129.7L34.3 125.2L28.2 119.8L22.8 113.7L18.3 107L14.7 99.7L12.1 92L10.5 84.1L10 76L10.5 67.9L12.1 60L14.7 52.3L18.3 45L22.8 38.3L28.2 32.2L34.3 26.8L41 22.3L48.3 18.7L56 16.1L63.9 14.5L72 14L80.1 14.5L88 16.1L95.7 18.7L103 22.3L109.7 26.8L115.8 32.2L121.2 38.3L125.7 45L129.3 52.3L131.9 60L133.5 67.9Z"/><path class="ln-m thin dash" d="M106 76L105.7 80.4L104.8 84.8L103.4 89L101.4 93L99 96.7L96 100L92.7 103L89 105.4L85 107.4L80.8 108.8L76.4 109.7L72 110L67.6 109.7L63.2 108.8L59 107.4L55 105.4L51.3 103L48 100L45 96.7L42.6 93L40.6 89L39.2 84.8L38.3 80.4L38 76L38.3 71.6L39.2 67.2L40.6 63L42.6 59L45 55.3L48 52L51.3 49L55 46.6L59 44.6L63.2 43.2L67.6 42.3L72 42L76.4 42.3L80.8 43.2L85 44.6L89 46.6L92.7 49L96 52L99 55.3L101.4 59L103.4 63L104.8 67.2L105.7 71.6Z"/><path class="c1 sw3" d="M55.0419 63.0413L76.9581 64.9587"/><path class="c1 sw3" d="M58.2218 56.2218L73.7782 71.7782"/><circle class="fi" cx="66" cy="64" r="2.2"/><path class="c2 sw3" d="M75.4114 96.5532L84.5886 83.4468"/><path class="c2 sw3" d="M72.2726 92.0706L87.7274 87.9294"/><circle class="fi" cx="80" cy="90" r="2.2"/><rect class="fi" x="20" y="70" width="4" height="12"/><rect class="fi" x="16" y="74" width="12" height="4"/><rect class="fi" x="120" y="70" width="4" height="12"/><rect class="fi" x="116" y="74" width="12" height="4"/><text class="tl tb" x="152" y="24">5  Prophase II</text><text class="tl" x="152" y="50">one of the two cells</text><text class="tl" x="152" y="64">no pairing this time</text><path class="ln-m thin" d="M148 46L84 64"/><text class="tl" x="152" y="96">nuclear envelope</text><text class="tl" x="152" y="110">breaking down</text><path class="ln-m thin" d="M148 92L102 98"/><text class="tl" x="152" y="134">new spindle forms</text><path class="ln-m thin" d="M148 130L126 80"/><path class="fp ln" d="M134 226L133.5 234.1L131.9 242L129.3 249.7L125.7 257L121.2 263.7L115.8 269.8L109.7 275.2L103 279.7L95.7 283.3L88 285.9L80.1 287.5L72 288L63.9 287.5L56 285.9L48.3 283.3L41 279.7L34.3 275.2L28.2 269.8L22.8 263.7L18.3 257L14.7 249.7L12.1 242L10.5 234.1L10 226L10.5 217.9L12.1 210L14.7 202.3L18.3 195L22.8 188.3L28.2 182.2L34.3 176.8L41 172.3L48.3 168.7L56 166.1L63.9 164.5L72 164L80.1 164.5L88 166.1L95.7 168.7L103 172.3L109.7 176.8L115.8 182.2L121.2 188.3L125.7 195L129.3 202.3L131.9 210L133.5 217.9Z"/><path class="c1 sw3" d="M60.8738 216.495L83.1262 207.505"/><path class="c1 sw3" d="M60.8738 207.505L83.1262 216.495"/><circle class="fi" cx="72" cy="212" r="2.2"/><path class="c2 sw3" d="M64.5825 242.997L79.4175 237.003"/><path class="c2 sw3" d="M64.5825 237.003L79.4175 242.997"/><circle class="fi" cx="72" cy="240" r="2.2"/><path class="ln-m thin" d="M20 226L69 212"/><path class="ln-m thin" d="M124 226L75 212"/><path class="ln-m thin" d="M20 226L69 240"/><path class="ln-m thin" d="M124 226L75 240"/><rect class="fi" x="18" y="220" width="4" height="12"/><rect class="fi" x="14" y="224" width="12" height="4"/><rect class="fi" x="122" y="220" width="4" height="12"/><rect class="fi" x="118" y="224" width="12" height="4"/><text class="tl tb" x="152" y="174">6  Metaphase II</text><text class="tl" x="152" y="200">chromosomes line up</text><text class="tl" x="152" y="214">singly on equator</text><path class="ln-m thin" d="M148 196L84 210"/><text class="tl" x="152" y="246">fibres from both</text><text class="tl" x="152" y="260">poles on each one</text><path class="ln-m thin" d="M148 242L102 235"/></svg><figcaption>Prophase II and metaphase II in one of the two haploid cells (drawings). There is no pairing: this division looks like mitosis, but the cell has only two chromosomes.</figcaption></figure>
:::

**Prophase II**
- If the chromosomes uncoiled, they condense again. There are no pairs this time.
- Any nuclear envelope breaks down and a new spindle forms in each of the two cells.

**Metaphase II**
- The chromosomes line up **singly** on the equator (not in pairs).
- Each chromosome is attached by its centromere to spindle fibres from **both** poles.

:::html
<figure class="fig small"><svg viewBox="0 0 330 300" role="img" aria-label="Two stages of meiosis II. Anaphase II: the centromeres divide and the chromatids are pulled to opposite poles. Telophase II: four cells, each with a nucleus containing two chromosomes."><path class="fp ln" d="M134 76L133.5 84.1L131.9 92L129.3 99.7L125.7 107L121.2 113.7L115.8 119.8L109.7 125.2L103 129.7L95.7 133.3L88 135.9L80.1 137.5L72 138L63.9 137.5L56 135.9L48.3 133.3L41 129.7L34.3 125.2L28.2 119.8L22.8 113.7L18.3 107L14.7 99.7L12.1 92L10.5 84.1L10 76L10.5 67.9L12.1 60L14.7 52.3L18.3 45L22.8 38.3L28.2 32.2L34.3 26.8L41 22.3L48.3 18.7L56 16.1L63.9 14.5L72 14L80.1 14.5L88 16.1L95.7 18.7L103 22.3L109.7 26.8L115.8 32.2L121.2 38.3L125.7 45L129.3 52.3L131.9 60L133.5 67.9Z"/><path class="c1 sw3" d="M48 62L65.659 52.6106"/><path class="c1 sw3" d="M48 62L65.659 71.3894"/><circle class="fi" cx="48" cy="62" r="2.2"/><path class="ln-m thin" d="M20 76L48 62"/><path class="c2 sw3" d="M48 90L59.4783 83.8969"/><path class="c2 sw3" d="M48 90L59.4783 96.1031"/><circle class="fi" cx="48" cy="90" r="2.2"/><path class="ln-m thin" d="M20 76L48 90"/><path class="c1 sw3" d="M96 62L78.341 52.6106"/><path class="c1 sw3" d="M96 62L78.341 71.3894"/><circle class="fi" cx="96" cy="62" r="2.2"/><path class="ln-m thin" d="M124 76L96 62"/><path class="c2 sw3" d="M96 90L84.5217 83.8969"/><path class="c2 sw3" d="M96 90L84.5217 96.1031"/><circle class="fi" cx="96" cy="90" r="2.2"/><path class="ln-m thin" d="M124 76L96 90"/><rect class="fi" x="18" y="70" width="4" height="12"/><rect class="fi" x="14" y="74" width="12" height="4"/><rect class="fi" x="122" y="70" width="4" height="12"/><rect class="fi" x="118" y="74" width="12" height="4"/><text class="tl tb" x="152" y="24">7  Anaphase II</text><text class="tl" x="152" y="50">centromeres divide</text><path class="ln-m thin" d="M148 46L96 60"/><text class="tl" x="152" y="82">chromatids pulled</text><text class="tl" x="152" y="96">to opposite poles</text><path class="ln-m thin" d="M148 78L102 88"/><path class="fp ln" d="M68 198L67.8 201.1L67.1 204.2L66 207.2L64.5 210L62.6 212.6L60.4 215L57.8 217L55 218.8L51.9 220.2L48.7 221.2L45.4 221.8L42 222L38.6 221.8L35.3 221.2L32.1 220.2L29 218.8L26.2 217L23.6 215L21.4 212.6L19.5 210L18 207.2L16.9 204.2L16.2 201.1L16 198L16.2 194.9L16.9 191.8L18 188.8L19.5 186L21.4 183.4L23.6 181L26.2 179L29 177.2L32.1 175.8L35.3 174.8L38.6 174.2L42 174L45.4 174.2L48.7 174.8L51.9 175.8L55 177.2L57.8 179L60.4 181L62.6 183.4L64.5 186L66 188.8L67.1 191.8L67.8 194.9Z"/><path class="ln" d="M55 198L54.9 199.7L54.6 201.4L54 203L53.3 204.5L52.3 205.9L51.2 207.2L49.9 208.3L48.5 209.3L47 210L45.4 210.6L43.7 210.9L42 211L40.3 210.9L38.6 210.6L37 210L35.5 209.3L34.1 208.3L32.8 207.2L31.7 205.9L30.7 204.5L30 203L29.4 201.4L29.1 199.7L29 198L29.1 196.3L29.4 194.6L30 193L30.7 191.5L31.7 190.1L32.8 188.8L34.1 187.7L35.5 186.7L37 186L38.6 185.4L40.3 185.1L42 185L43.7 185.1L45.4 185.4L47 186L48.5 186.7L49.9 187.7L51.2 188.8L52.3 190.1L53.3 191.5L54 193L54.6 194.6L54.9 196.3Z"/><path class="c1 sw2" d="M36 195L48 195"/><path class="c2 sw2" d="M38 202L46 202"/><path class="fp ln" d="M68 254L67.8 257.1L67.1 260.2L66 263.2L64.5 266L62.6 268.6L60.4 271L57.8 273L55 274.8L51.9 276.2L48.7 277.2L45.4 277.8L42 278L38.6 277.8L35.3 277.2L32.1 276.2L29 274.8L26.2 273L23.6 271L21.4 268.6L19.5 266L18 263.2L16.9 260.2L16.2 257.1L16 254L16.2 250.9L16.9 247.8L18 244.8L19.5 242L21.4 239.4L23.6 237L26.2 235L29 233.2L32.1 231.8L35.3 230.8L38.6 230.2L42 230L45.4 230.2L48.7 230.8L51.9 231.8L55 233.2L57.8 235L60.4 237L62.6 239.4L64.5 242L66 244.8L67.1 247.8L67.8 250.9Z"/><path class="ln" d="M55 254L54.9 255.7L54.6 257.4L54 259L53.3 260.5L52.3 261.9L51.2 263.2L49.9 264.3L48.5 265.3L47 266L45.4 266.6L43.7 266.9L42 267L40.3 266.9L38.6 266.6L37 266L35.5 265.3L34.1 264.3L32.8 263.2L31.7 261.9L30.7 260.5L30 259L29.4 257.4L29.1 255.7L29 254L29.1 252.3L29.4 250.6L30 249L30.7 247.5L31.7 246.1L32.8 244.8L34.1 243.7L35.5 242.7L37 242L38.6 241.4L40.3 241.1L42 241L43.7 241.1L45.4 241.4L47 242L48.5 242.7L49.9 243.7L51.2 244.8L52.3 246.1L53.3 247.5L54 249L54.6 250.6L54.9 252.3Z"/><path class="c1 sw2" d="M36 251L48 251"/><path class="c2 sw2" d="M38 258L46 258"/><path class="fp ln" d="M128 198L127.8 201.1L127.1 204.2L126 207.2L124.5 210L122.6 212.6L120.4 215L117.8 217L115 218.8L111.9 220.2L108.7 221.2L105.4 221.8L102 222L98.6 221.8L95.3 221.2L92.1 220.2L89 218.8L86.2 217L83.6 215L81.4 212.6L79.5 210L78 207.2L76.9 204.2L76.2 201.1L76 198L76.2 194.9L76.9 191.8L78 188.8L79.5 186L81.4 183.4L83.6 181L86.2 179L89 177.2L92.1 175.8L95.3 174.8L98.6 174.2L102 174L105.4 174.2L108.7 174.8L111.9 175.8L115 177.2L117.8 179L120.4 181L122.6 183.4L124.5 186L126 188.8L127.1 191.8L127.8 194.9Z"/><path class="ln" d="M115 198L114.9 199.7L114.6 201.4L114 203L113.3 204.5L112.3 205.9L111.2 207.2L109.9 208.3L108.5 209.3L107 210L105.4 210.6L103.7 210.9L102 211L100.3 210.9L98.6 210.6L97 210L95.5 209.3L94.1 208.3L92.8 207.2L91.7 205.9L90.7 204.5L90 203L89.4 201.4L89.1 199.7L89 198L89.1 196.3L89.4 194.6L90 193L90.7 191.5L91.7 190.1L92.8 188.8L94.1 187.7L95.5 186.7L97 186L98.6 185.4L100.3 185.1L102 185L103.7 185.1L105.4 185.4L107 186L108.5 186.7L109.9 187.7L111.2 188.8L112.3 190.1L113.3 191.5L114 193L114.6 194.6L114.9 196.3Z"/><path class="c1 sw2" d="M96 195L108 195"/><path class="c2 sw2" d="M98 202L106 202"/><path class="fp ln" d="M128 254L127.8 257.1L127.1 260.2L126 263.2L124.5 266L122.6 268.6L120.4 271L117.8 273L115 274.8L111.9 276.2L108.7 277.2L105.4 277.8L102 278L98.6 277.8L95.3 277.2L92.1 276.2L89 274.8L86.2 273L83.6 271L81.4 268.6L79.5 266L78 263.2L76.9 260.2L76.2 257.1L76 254L76.2 250.9L76.9 247.8L78 244.8L79.5 242L81.4 239.4L83.6 237L86.2 235L89 233.2L92.1 231.8L95.3 230.8L98.6 230.2L102 230L105.4 230.2L108.7 230.8L111.9 231.8L115 233.2L117.8 235L120.4 237L122.6 239.4L124.5 242L126 244.8L127.1 247.8L127.8 250.9Z"/><path class="ln" d="M115 254L114.9 255.7L114.6 257.4L114 259L113.3 260.5L112.3 261.9L111.2 263.2L109.9 264.3L108.5 265.3L107 266L105.4 266.6L103.7 266.9L102 267L100.3 266.9L98.6 266.6L97 266L95.5 265.3L94.1 264.3L92.8 263.2L91.7 261.9L90.7 260.5L90 259L89.4 257.4L89.1 255.7L89 254L89.1 252.3L89.4 250.6L90 249L90.7 247.5L91.7 246.1L92.8 244.8L94.1 243.7L95.5 242.7L97 242L98.6 241.4L100.3 241.1L102 241L103.7 241.1L105.4 241.4L107 242L108.5 242.7L109.9 243.7L111.2 244.8L112.3 246.1L113.3 247.5L114 249L114.6 250.6L114.9 252.3Z"/><path class="c1 sw2" d="M96 251L108 251"/><path class="c2 sw2" d="M98 258L106 258"/><text class="tl tb" x="152" y="174">8  Telophase II</text><text class="tl" x="152" y="200">four cells (two from</text><text class="tl" x="152" y="214">each cell of meiosis I)</text><path class="ln-m thin" d="M148 196L120 192"/><text class="tl" x="152" y="246">each nucleus is</text><text class="tl" x="152" y="260">haploid (n = 2)</text><path class="ln-m thin" d="M148 242L108 250"/></svg><figcaption>Anaphase II and telophase II. Each chromatid is now a chromosome. Meiosis I and II together make four haploid cells from one diploid cell.</figcaption></figure>
:::

**Anaphase II**
- The centromeres **divide**, so the sister chromatids separate. Each is now a chromosome.
- The spindle fibres shorten and pull the chromosomes to opposite poles, centromere first.

**Telophase II**
- The chromosomes reach the poles and uncoil. A nuclear envelope forms around each group and the spindle breaks down.
- The cell surface membrane pinches in (a cell wall forms in plants) and the cytoplasm divides again.
- The result is **four haploid cells**. In a male animal all four develop into sperm. In a female animal the cytoplasm divides unequally, so one large cell becomes the egg and the small cells do not develop.

:::key The two divisions in one line each
- **Meiosis I**: homologous chromosomes pair up (bivalents), cross over, line up in pairs, and are pulled apart. Chromosome number: 2n to n.
- **Meiosis II**: sister chromatids are pulled apart, as in mitosis. Chromosome number stays at n, and each chromosome becomes a single chromatid.
:::

### Counting chromosomes, chromatids and DNA

The counting rule from [Chromosomes and the mitotic cell cycle](#bio.mitosis) still holds: a chromosome with two chromatids is **one chromosome**, and it holds two DNA molecules. This table follows a human cell, 2n = 46.

| stage | chromosomes per cell | chromatids per cell | DNA molecules per cell |
|---|---|---|---|
| G1 (before S phase) | 46 | 0 | 46 |
| prophase I, metaphase I, anaphase I | 46 | 92 | 92 |
| each cell after telophase I | 23 | 46 | 46 |
| prophase II, metaphase II (each cell) | 23 | 46 | 46 |
| anaphase II (each cell) | 46 | 0 | 46 |
| each cell after telophase II | 23 | 0 | 23 |

The chromosome number halves in **meiosis I**, not meiosis II. During anaphase II the number briefly doubles in each cell, as in mitosis, and then returns to 23 when the cell divides.

:::warn Meiosis II does not halve the chromosome number
Meiosis I halves it, because whole chromosomes (one of each pair) go to each new cell. Meiosis II separates chromatids, so each of its four cells ends with the same number of chromosomes (23) as the two cells before it. The DNA content per cell does halve again, because each chromosome stops being two chromatids.
:::

:::eg A cell with 2n = 12 starts meiosis. Complete a table of the number of chromosomes, chromatids and DNA molecules in one cell at the stages shown.
**Start from the counting rule.** In G1 each of the 12 chromosomes is a single DNA molecule with no chromatids. After S phase every chromosome is two chromatids.

| stage | chromosomes | chromatids | DNA molecules |
|---|---|---|---|
| G1 | 12 | 0 | 12 |
| metaphase I | 12 | 24 | 24 |
| after meiosis I (each cell) | 6 | 12 | 12 |
| anaphase II (each cell) | 12 | 0 | 12 |
| after meiosis II (each cell) | 6 | 0 | 6 |

**Why each row.** DNA replication doubles the DNA from 12 to 24 molecules, but the chromosomes are still 12. In meiosis I the 6 homologous pairs separate, so each cell gets 6 chromosomes, each with two chromatids, and so 12 DNA molecules. In anaphase II the chromatids separate, so each chromatid counts as a chromosome and there are 12 for a moment in each cell. After telophase II each of the four cells has 6 chromosomes and 6 DNA molecules: half of the original 12.
:::

### The DNA content of a cell

A graph of the DNA content of one cell shows the same story. DNA doubles in S phase, halves when the cell divides at the end of meiosis I, and halves again at the end of meiosis II.

:::plot DNA content of a cell through meiosis. The content doubles from 2 to 4 units in S phase, halves to 2 units at the end of meiosis I, and halves again to 1 unit at the end of meiosis II.
--f "2+2/(1+exp(0-(x-6)*3))-2/(1+exp(0-(x-16)*3))-1/(1+exp(0-(x-24)*3))" --label "DNA per cell" --x 0 30 --y 0 5.5 --xlabel "time / arbitrary units" --ylabel "DNA content / arbitrary units" --pt "11,4,DNA copied (S phase)@n" --pt "20,2,meiosis I over@ne" --pt "28,1,meiosis II over@ne" --legend tr --alt "The DNA content is 2 units, rises steeply to 4 units around time 6, stays at 4, falls steeply to 2 units around time 16, stays at 2, and falls steeply to 1 unit around time 24."
:::

:::eg Describe and explain the changes in the DNA content of the cell shown in the graph.
Describe first, with figures, then explain each change.

The DNA content doubles from 2 to 4 units at about time 6. [B1]

It halves from 4 to 2 units at about time 16, and halves again from 2 to 1 unit at about time 24. [B1]

The doubling is DNA replication in S phase, which makes each chromosome two chromatids. [B1]

The first fall is the end of meiosis I: homologous chromosomes separate into two cells, so each cell has half of the DNA. [B1]

The second fall is the end of meiosis II: sister chromatids separate into four cells, so each has half again. [B1]

(Also credit: the DNA content stays at 4 units between replication and the end of meiosis I because no DNA is made or lost in prophase, metaphase or anaphase.)

A weaker answer says "the DNA goes up and then down in steps". It quotes no figures, does not link each step to a stage and does not name replication or the separation of homologues and chromatids.
:::

## Telling meiosis from mitosis in photomicrographs and diagrams

Exam questions show a drawing or a photomicrograph and ask you to name the stage. In a real photomicrograph the chromosomes are stained darkest and look like short rods or X-shapes; the spindle fibres are hard to see. Work out the stage with these questions, in this order.

:::steps
1. **Is there a nuclear envelope?** If a clear nucleus with a nuclear envelope is present and the chromosomes are not condensed, the cell is in interphase or telophase. If the chromosomes are condensed and there is no envelope, go on.
2. **Are the chromosomes in pairs?** Pairs (bivalents) side by side mean **meiosis I** (prophase I or metaphase I). Chromosomes on their own mean mitosis or meiosis II.
3. **Where are they?** Scattered: prophase. On the equator: metaphase. Moving to the poles: anaphase. At the poles in groups: telophase.
4. **What is moving in anaphase?** Whole chromosomes with **two** chromatids each means anaphase I. Single chromatids (V-shapes) means anaphase II or mitosis.
5. **How many chromosomes at each pole, compared with the body cell?** In mitosis each pole receives the full diploid number (2n). In anaphase I and anaphase II each pole receives n.
:::

The last step separates anaphase II from anaphase of mitosis, which look alike. If the cell has 2n = 8, a pole in mitosis receives 8 chromatids and a pole in anaphase II receives only 4.

| stage | chromosomes in pairs? | what moves | sister chromatids |
|---|---|---|---|
| prophase I | yes, bivalents form | nothing yet | joined |
| metaphase I | yes, on the equator | nothing | joined |
| anaphase I | no, the pairs have just separated | whole chromosomes | joined |
| metaphase II | no, singly on the equator | nothing | joined |
| anaphase II | no | single chromatids | separated |

:::eg Four cells from the anther of a plant with 2n = 6 were examined. Name the stage of meiosis of each cell from the description.
| cell | description |
|---|---|
| P | no nuclear envelope; chromosomes lie in three pairs, with crossing points visible between the two chromosomes of each pair |
| Q | six chromosomes, each of two chromatids, being pulled apart: three move towards each pole |
| R | three chromosomes, each of two chromatids, lie singly on the equator |
| S | four cells joined together, each with a nuclear envelope around three chromosomes, each chromosome a single chromatid |

**P** is **prophase I**: no envelope, chromosomes paired in bivalents, and crossing points (chiasmata) are visible. [B1]

**Q** is **anaphase I**: whole chromosomes of two chromatids are separating, and the 6 chromosomes are split into groups of 3 (the haploid number). [B1]

**R** is **metaphase II**: the chromosomes are not in pairs and each still has two chromatids, so this is a haploid cell about to separate its chromatids. [B1]

**S** is **telophase II** (the end of meiosis): four haploid cells, each with 3 chromosomes, and now single chromatids. [B1]

Check the numbers: 3 chromosomes in each cell of S is n = 3, half of 2n = 6.
:::

:::exam Drawing and naming stages
You may be asked to draw a stage or to state the number of chromosomes. Draw chromosomes with two chromatids and a centromere, show pairs only in prophase I and metaphase I, and state the number of chromosomes (not chromatids) in each cell. Name the stage with its I or II: "anaphase" alone does not score for meiosis.
:::

## How meiosis makes gametes genetically different

Meiosis and fertilisation produce genetic variation in three ways: crossing over, random orientation (independent assortment) and random fertilisation. Mutation, a change in DNA, is a further source of new alleles but is a different process.

### Crossing over

:::def Crossing over
The exchange of sections of DNA between non-sister chromatids of a homologous pair during prophase I of meiosis, which produces new combinations of alleles on the chromatids.
:::

In prophase I, homologous chromosomes lie side by side as a bivalent. Two **non-sister chromatids**, one from each chromosome, break at the same point and each joins to the other's cut end. The points at which they stay joined are the chiasmata.

:::html
<figure class="fig small"><svg viewBox="0 0 330 400" role="img" aria-label="Crossing over in two steps. Step 1: two homologous chromosomes, each of two sister chromatids, lie side by side. The maternal chromosome carries alleles A and B and the paternal carries a and b. Two non-sister chromatids cross at a chiasma and exchange sections. Step 2: the four chromatids after crossing over carry AB, Ab, aB and ab. AB and ab are the parental combinations; Ab and aB are new combinations."><text class="tl tb" x="8" y="16">1  A chiasma forms</text><path class="c1 sw3" d="M40 52L40 132"/><path class="c2 sw3" d="M170 52L170 132"/><path class="c1 sw3" d="M64 52L64 76L105 92"/><path class="c2 sw3" d="M105 92L146 108L146 132"/><path class="c2 sw3" d="M146 52L146 76L105 92"/><path class="c1 sw3" d="M105 92L64 108L64 132"/><text class="tl" x="40" y="44" text-anchor="middle">A</text><text class="tl" x="40" y="148" text-anchor="middle">B</text><text class="tl" x="64" y="44" text-anchor="middle">A</text><text class="tl" x="64" y="148" text-anchor="middle">B</text><text class="tl" x="146" y="44" text-anchor="middle">a</text><text class="tl" x="146" y="148" text-anchor="middle">b</text><text class="tl" x="170" y="44" text-anchor="middle">a</text><text class="tl" x="170" y="148" text-anchor="middle">b</text><text class="tl" x="105" y="130" text-anchor="middle">chiasma</text><path class="ln-m thin" d="M105 116L105 95"/><text class="tl" x="196" y="74">non-sister</text><text class="tl" x="196" y="88">chromatids break</text><text class="tl" x="196" y="102">and rejoin</text><text class="tl tb" x="8" y="196">2  After crossing over</text><path class="c1 sw3" d="M46 232L46 272"/><path class="c1 sw3" d="M46 272L46 312"/><text class="tl" x="46" y="224" text-anchor="middle">A</text><text class="tl" x="46" y="328" text-anchor="middle">B</text><text class="tl tb" x="46" y="350" text-anchor="middle">AB</text><path class="c1 sw3" d="M110 232L110 272"/><path class="c2 sw3" d="M110 272L110 312"/><text class="tl" x="110" y="224" text-anchor="middle">A</text><text class="tl" x="110" y="328" text-anchor="middle">b</text><text class="tl tb" x="110" y="350" text-anchor="middle">Ab</text><path class="c2 sw3" d="M174 232L174 272"/><path class="c1 sw3" d="M174 272L174 312"/><text class="tl" x="174" y="224" text-anchor="middle">a</text><text class="tl" x="174" y="328" text-anchor="middle">B</text><text class="tl tb" x="174" y="350" text-anchor="middle">aB</text><path class="c2 sw3" d="M238 232L238 272"/><path class="c2 sw3" d="M238 272L238 312"/><text class="tl" x="238" y="224" text-anchor="middle">a</text><text class="tl" x="238" y="328" text-anchor="middle">b</text><text class="tl tb" x="238" y="350" text-anchor="middle">ab</text><text class="tl" x="8" y="372">AB and ab: parental combinations</text><text class="tl" x="8" y="388">Ab and aB: new combinations</text></svg><figcaption>Crossing over (a drawing; a line style change marks the exchanged section). Before it, the four chromatids carry only AB or ab. After it, two of them carry new combinations of alleles, Ab and aB.</figcaption></figure>
:::

Before crossing over, one chromosome has alleles A and B on both its chromatids, and the homologue has a and b. After one crossing over between the two loci, the four chromatids carry AB, Ab, aB and ab. Two are the original **parental combinations** and two are **new combinations**, which did not exist in either parent. A gamete that receives a chromatid with a new combination is genetically different from both parents' own gametes.

Every chromatid pair crosses over at random positions, so there are huge numbers of possible combinations along a chromosome.

:::warn Crossing over is between non-sister chromatids
Sister chromatids are identical copies, so exchanging sections between them changes nothing. Crossing over is between one chromatid of each homologue. Also, crossing over and independent assortment are two different events: crossing over swaps sections of chromatids in prophase I; independent assortment is the random way the pairs line up in metaphase I.
:::

### Random orientation (independent assortment)

In metaphase I the bivalents line up on the equator. Which chromosome of a pair (the maternal or the paternal one) faces which pole is **random**, and it is decided separately for each pair. So the chromosomes you inherited from your mother and father are shuffled into new sets.

:::html
<figure class="fig small"><svg viewBox="0 0 330 272" role="img" aria-label="Random orientation of two homologous pairs at metaphase I. In orientation 1 the A and B chromosomes face the same pole, giving gametes AB and ab. In orientation 2 the A and b chromosomes face the same pole, giving gametes Ab and aB."><text class="tl tb" x="82" y="22" text-anchor="middle">Orientation 1</text><path class="fp ln" d="M152 104L151.4 111.6L149.6 119L146.7 126.2L142.6 133L137.5 139.3L131.5 145L124.6 150L117 154.2L108.8 157.6L100.1 160L91.1 161.5L82 162L72.9 161.5L63.9 160L55.2 157.6L47 154.2L39.4 150L32.5 145L26.5 139.3L21.4 133L17.3 126.2L14.4 119L12.6 111.6L12 104L12.6 96.4L14.4 89L17.3 81.8L21.4 75L26.5 68.7L32.5 63L39.4 58L47 53.8L55.2 50.4L63.9 48L72.9 46.5L82 46L91.1 46.5L100.1 48L108.8 50.4L117 53.8L124.6 58L131.5 63L137.5 68.7L142.6 75L146.7 81.8L149.6 89L151.4 96.4Z"/><path class="c1 sw3" d="M59.801 90.1207L80.199 81.8793"/><path class="c1 sw3" d="M59.801 81.8793L80.199 90.1207"/><circle class="fi" cx="70" cy="86" r="2.2"/><path class="c1 sw3" d="M83.801 90.1207L104.199 81.8793"/><path class="c1 sw3" d="M83.801 81.8793L104.199 90.1207"/><circle class="fi" cx="94" cy="86" r="2.2"/><text class="tl" x="50" y="90" text-anchor="end">A</text><text class="tl" x="114" y="90">a</text><path class="c2 sw3" d="M62.5825 124.997L77.4175 119.003"/><path class="c2 sw3" d="M62.5825 119.003L77.4175 124.997"/><circle class="fi" cx="70" cy="122" r="2.2"/><path class="c2 sw3" d="M86.5825 124.997L101.417 119.003"/><path class="c2 sw3" d="M86.5825 119.003L101.417 124.997"/><circle class="fi" cx="94" cy="122" r="2.2"/><text class="tl" x="50" y="126" text-anchor="end">B</text><text class="tl" x="114" y="126">b</text><path class="ln" d="M82 178L82 192" marker-end="url(#ah)"/><text class="tl" x="82" y="212" text-anchor="middle">gametes AB and ab</text><text class="tl tb" x="248" y="22" text-anchor="middle">Orientation 2</text><path class="fp ln" d="M318 104L317.4 111.6L315.6 119L312.7 126.2L308.6 133L303.5 139.3L297.5 145L290.6 150L283 154.2L274.8 157.6L266.1 160L257.1 161.5L248 162L238.9 161.5L229.9 160L221.2 157.6L213 154.2L205.4 150L198.5 145L192.5 139.3L187.4 133L183.3 126.2L180.4 119L178.6 111.6L178 104L178.6 96.4L180.4 89L183.3 81.8L187.4 75L192.5 68.7L198.5 63L205.4 58L213 53.8L221.2 50.4L229.9 48L238.9 46.5L248 46L257.1 46.5L266.1 48L274.8 50.4L283 53.8L290.6 58L297.5 63L303.5 68.7L308.6 75L312.7 81.8L315.6 89L317.4 96.4Z"/><path class="c1 sw3" d="M225.801 90.1207L246.199 81.8793"/><path class="c1 sw3" d="M225.801 81.8793L246.199 90.1207"/><circle class="fi" cx="236" cy="86" r="2.2"/><path class="c1 sw3" d="M249.801 90.1207L270.199 81.8793"/><path class="c1 sw3" d="M249.801 81.8793L270.199 90.1207"/><circle class="fi" cx="260" cy="86" r="2.2"/><text class="tl" x="216" y="90" text-anchor="end">A</text><text class="tl" x="280" y="90">a</text><path class="c2 sw3" d="M228.583 124.997L243.417 119.003"/><path class="c2 sw3" d="M228.583 119.003L243.417 124.997"/><circle class="fi" cx="236" cy="122" r="2.2"/><path class="c2 sw3" d="M252.583 124.997L267.417 119.003"/><path class="c2 sw3" d="M252.583 119.003L267.417 124.997"/><circle class="fi" cx="260" cy="122" r="2.2"/><text class="tl" x="216" y="126" text-anchor="end">b</text><text class="tl" x="280" y="126">B</text><path class="ln" d="M248 178L248 192" marker-end="url(#ah)"/><text class="tl" x="248" y="212" text-anchor="middle">gametes Ab and aB</text><text class="tl" x="165" y="244" text-anchor="middle">metaphase I, no crossing over:</text><text class="tl" x="165" y="260" text-anchor="middle">four kinds of gamete in all</text></svg><figcaption>Two possible orientations of the same two pairs (drawings, no crossing over). Which way round the second pair lies does not depend on the first, so both orientations are equally likely.</figcaption></figure>
:::

With two pairs there are two equally likely orientations, giving four kinds of gamete: AB, ab, Ab and aB. With three pairs there are \(2 \times 2 \times 2 = 8\) kinds of gamete. In general:

:::key Combinations from random orientation
For a diploid cell with \(n\) homologous pairs, the number of different combinations of maternal and paternal chromosomes in the gametes is \(2^n\) (ignoring crossing over). In humans, \(n = 23\), so \(2^{23} = 8\,388\,608\), or about 8.4 million.
:::

Random orientation also happens in **metaphase II**. Crossing over has made the two sister chromatids of a chromosome different from each other, so which chromatid goes to which pole in anaphase II is random too. This adds even more variation.

:::eg A cell has 2n = 6. Calculate the number of different combinations of chromosomes in the gametes, and in the zygotes made when gametes from two such individuals fuse at random. Ignore crossing over.
**Gametes.** The haploid number is \(n = 6 \div 2 = 3\), so there are 3 homologous pairs. [M1]

Number of combinations in gametes:

\[\begin{aligned} 2^n &= 2^3 \\ &= 8 \end{aligned}\]

[A1]

**Zygotes.** Any of the 8 types of gamete from one parent can fuse with any of the 8 types from the other. [M1]

\[\begin{aligned} 8 \times 8 &= 2^3 \times 2^3 \\ &= 64 \end{aligned}\]

[A1]

Crossing over would add many more. The formula only counts shuffling of whole chromosomes, so the true number of different gametes is much larger.
:::

### Random fertilisation

:::def Random fertilisation
The fusion of any one male gamete with any one female gamete, chosen by chance, so that each zygote has a new combination of alleles from the two parents.
:::

A human male makes millions of sperm and a female makes eggs, and each gamete is genetically different. Which sperm reaches which egg is down to chance. From random orientation alone, there are \(2^{23}\) kinds of sperm and \(2^{23}\) kinds of egg, so the number of different zygotes a couple could produce is:

\[\begin{aligned} 2^{23} \times 2^{23} &= 2^{46} \\ &\approx 7.0 \times 10^{13} \end{aligned}\]

That is about 70 million million, before crossing over is even counted. This is why brothers and sisters (apart from identical twins) differ, and why your genotype has probably never existed before.

:::analogy Shuffling two packs of cards
Meiosis is like shuffling a pack of cards. Random orientation shuffles whole chromosomes between the two gametes' piles. Crossing over cuts each card in half and swaps the halves. Random fertilisation then deals one hand from each parent together. A new hand is almost certain.
:::

:::key How genetic variation arises
- **Crossing over** (prophase I): non-sister chromatids exchange sections, making new combinations of alleles on a chromosome.
- **Random orientation / independent assortment** (metaphase I, and metaphase II): the pairs of homologous chromosomes, and the chromatids, are arranged and separated at random, so gametes differ in which chromosomes they get.
- **Random fertilisation**: any male gamete can fuse with any female gamete, so zygotes differ.
:::

:::eg Explain how meiosis and fertilisation produce genetically different offspring from the same two parents.
A full answer gives six separate marking points.

During prophase I, homologous chromosomes pair up and non-sister chromatids exchange sections by crossing over. [B1]

This gives new combinations of alleles on the chromatids. [B1]

In metaphase I the pairs of homologous chromosomes line up at random on the equator, so each gamete gets a random mixture of maternal and paternal chromosomes (independent assortment). [B1]

In metaphase II the chromatids, which now differ because of crossing over, are also arranged at random. [B1]

So each gamete is genetically different. [B1]

At fertilisation, any male gamete can fuse with any female gamete, at random, so each zygote has a different combination of alleles. [B1]

(Also credit: the number of combinations is \(2^n\) for \(n\) pairs of chromosomes; mutation is a source of new alleles.)

A weaker answer says "meiosis mixes up the genes, so the babies are all different". It names none of the three processes, so it scores at most one mark.
:::

## Mitosis and meiosis compared

:::cols
:::col Mitosis
- One division.
- Makes **two** daughter cells.
- Daughter cells are **diploid** (2n), genetically **identical** to the parent.
- Homologous chromosomes do **not** pair up. No crossing over.
- Chromosomes line up **singly** in metaphase.
- **Chromatids** separate in anaphase.
- Used for growth, repair and asexual reproduction.
:::
:::col Meiosis
- **Two** divisions.
- Makes **four** daughter cells.
- Daughter cells are **haploid** (n), genetically **different** from each other and the parent.
- Homologous chromosomes **pair up** (bivalents) and cross over.
- Bivalents line up in **pairs** in metaphase I.
- **Homologous chromosomes** separate in anaphase I; chromatids in anaphase II.
- Used to make gametes (or spores).
:::
:::

:::eg Spot the error: describe the behaviour of the chromosomes in anaphase I. [3]
A student wrote this answer.

Line 1: The spindle fibres shorten and pull the chromosomes to the poles.
Line 2: The centromeres divide, so the sister chromatids separate.
Line 3: Each pole receives half of the chromosomes, one from each homologous pair.

Line 1 is correct [B1]. **Line 2 is wrong: the centromeres divide in anaphase II (and in mitosis), not in anaphase I. In anaphase I the centromeres stay intact and whole chromosomes, each with two chromatids, move to the poles, so the homologous chromosomes are what separate. That mark is lost [B0].** Line 3 is correct [B1].

Correct Line 2: "The homologous chromosomes of each pair separate, and the centromeres do not divide." With that change the answer scores 3 marks.
:::

:::eg Real context, microscope work: a student squashed an anther from a lily bud (2n = 24) and a root tip from a lily bulb. Explain why the anther was used to see meiosis, and what the student expects to count at metaphase I and at metaphase of mitosis.
Meiosis happens only in cells that will make gametes or spores, and in a flowering plant those cells are in the anther (which makes pollen). [B1]

A root tip is full of cells dividing by mitosis for growth, so it shows no meiosis. [B1]

At metaphase I the student expects to see 12 bivalents, because the 24 chromosomes form 12 homologous pairs. [B1]

At metaphase of mitosis the student expects 24 separate chromosomes, each of two chromatids, because the pairs do not join up in mitosis. [B1]

To see these, the squash is stained so that the chromosomes are darkest, and the student must look for pairs of chromosomes with crossing points, not single ones.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State the meaning of the term diploid and give the diploid number for humans.
A: A diploid cell has two complete sets of chromosomes, one set from each parent, so its chromosomes are in homologous pairs. In humans 2n = 46.
Q: State the haploid number of a cell from a species with 2n = 18.
A: \(n = 18 \div 2 = 9\).
Q: Explain why the gametes of an animal must be haploid.
A: Gametes fuse at fertilisation. If they were diploid, the zygote would have twice the parents' number of chromosomes, and the number would keep doubling each generation. Haploid gametes restore the diploid number.
Q: State two things that happen to the chromosomes in prophase I that do not happen in prophase of mitosis.
A: Homologous chromosomes pair up to form bivalents, and non-sister chromatids exchange sections (crossing over) at chiasmata.
Q: Name the stage of meiosis in which the chromosome number per cell halves, and state what happens to cause this.
A: Anaphase I (completed at telophase I). The homologous chromosomes of each pair are pulled to opposite poles, so each new cell has one chromosome of each pair.
Q: A cell with 2n = 8 is in metaphase II. State the number of chromosomes and the number of chromatids in the cell.
A: 4 chromosomes (n = 4), each of two chromatids, so 8 chromatids.
Q: State what is meant by a chiasma.
A: The point where two non-sister chromatids of a pair of homologous chromosomes are joined after crossing over. It is visible in prophase I and metaphase I.
Q: Calculate the number of different combinations of chromosomes in the gametes of an organism with 2n = 10, ignoring crossing over.
A: \(n = 5\), so the number is \(2^5 = 32\).
Q: Explain why crossing over between sister chromatids does not produce variation.
A: Sister chromatids are identical copies, with the same alleles at every locus. Swapping sections between them leaves every allele combination unchanged.
Q: Give two differences between the gametes produced by one individual and the cells produced by mitosis in the same individual.
A: Gametes are haploid, but cells made by mitosis are diploid. Gametes are genetically different from each other, but cells made by mitosis are identical.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State two differences between a pair of homologous chromosomes and a pair of sister chromatids.
A: Homologous chromosomes are one maternal and one paternal chromosome, with the same genes in the same order but possibly different alleles. [B1]
Sister chromatids are two identical copies of one chromosome, made by DNA replication and joined at a centromere, with the same alleles. [B1]
(Also credit: homologous chromosomes pair up in meiosis I; sister chromatids separate in meiosis II.)
Q: [4 marks] ★ A mouse has 2n = 40. (a) Calculate the number of different combinations of chromosomes in its gametes, ignoring crossing over. (b) Calculate the number of different zygotes from the random fusion of gametes of two unrelated mice, ignoring crossing over. Give your answer to (b) in standard form to two significant figures.
H: The haploid number is half of 2n. The number of combinations is 2 raised to the haploid number.
A: (a) \(n = 20\), so combinations \(= 2^{20}\) [M1] \(= 1\,048\,576\) [A1]
(b) \(2^{20} \times 2^{20} = 2^{40}\) [M1] \(= 1.1 \times 10^{12}\) [A1]
Q: [4 marks] ★★ A cell from an animal with 2n = 8 is described at two stages. In cell X four pairs of chromosomes lie on the equator, and each chromosome has two chromatids. In cell Y the chromatids are separated, and four single chromatids are moving to each pole. (a) Name the stage of X and the stage of Y. (b) State why cell Y cannot be in anaphase of mitosis.
H: In mitosis, how many chromatids would move towards each pole in a cell with 2n = 8?
A: (a) X is metaphase I. [B1] Y is anaphase II. [B1]
(b) In anaphase of mitosis, eight chromatids would move to each pole (the diploid number). [B1] Here only four move to each pole (the haploid number), so the cell has already been through meiosis I. [B1]
Q: [5 marks] ★★ A body cell of an animal contains 5.4 pg of DNA in G1. (a) Calculate the DNA content of a cell at metaphase I, of a cell at the end of telophase I, and of a sperm cell. (b) Explain why the DNA content of the zygote is the same as that of a body cell in G1.
H: S phase doubles the DNA. Meiosis I and meiosis II each halve it per cell.
A: (a) Metaphase I: \(2 \times 5.4 = 10.8\,\mathrm{pg}\) [B1]. After telophase I: \(10.8 \div 2 = 5.4\,\mathrm{pg}\) [B1]. Sperm: \(5.4 \div 2 = 2.7\,\mathrm{pg}\) [B1]
(b) The sperm and the egg are each haploid, with half of the DNA of a body cell. [B1] They fuse at fertilisation, so the zygote has the DNA of 2 haploid cells, which equals 5.4 pg. [B1]
Q: [4 marks] ★★ A cell is heterozygous for two genes on one pair of chromosomes. One chromosome carries alleles E and F and its homologue carries alleles e and f. In prophase I one crossing over occurs between the two loci. (a) State the combinations of alleles on the four chromatids afterwards. (b) Explain why a gamete containing the chromatid Ef is genetically different from a gamete formed with no crossing over.
H: Crossing over exchanges the parts of the chromatids beyond the point where they break.
A: (a) EF and ef (parental combinations) [B1] and Ef and eF (new combinations) [B1]
(b) Crossing over exchanged sections between non-sister chromatids, so alleles E and f are now on the same chromatid. [B1] This combination was not present on either parental chromosome, so the gamete is different from one made without crossing over. [B1]
Q: [3 marks] ★★ Describe three differences between the behaviour of the chromosomes in meiosis I and in mitosis.
A: Homologous chromosomes pair up to form bivalents in meiosis I, but not in mitosis. [B1]
Crossing over occurs between non-sister chromatids in meiosis I but not in mitosis. [B1]
Bivalents line up in pairs on the equator in metaphase I, but single chromosomes line up in mitosis. [B1]
(Also credit: whole chromosomes (homologues) separate in anaphase I but chromatids separate in anaphase of mitosis; the centromeres divide in mitosis but not in anaphase I.)
Q: [6 marks] ★★★ Identical twins are genetically identical to each other. Non-identical siblings born to the same parents are not. Explain these observations, using your knowledge of mitosis and meiosis.
H: Identical twins start as one fertilised egg. Think about which division separates the early cells.
H: For the siblings, think of all the sources of variation from meiosis, and of fertilisation.
A: Identical twins come from one zygote, whose cells separate into two early embryos. [B1]
The cells formed by mitosis from the zygote have identical DNA, so the twins have the same alleles. [B1]
Non-identical siblings come from different gametes, each made by meiosis. Crossing over gives new combinations of alleles in the gametes. [B1]
Random orientation of the homologous pairs in metaphase I (and of chromatids in metaphase II) means each gamete has a different mix of chromosomes. [B1]
Random fertilisation means any sperm can fuse with any egg. [B1]
So the zygotes of non-identical siblings have different combinations of alleles from the same parents. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ Down syndrome is usually caused by a person having three copies of chromosome 21 (47 chromosomes in each cell). It arises when a gamete has an extra chromosome 21 because the chromosomes fail to separate during meiosis. (a) Suppose the two homologues of chromosome 21 both move to the same pole in anaphase I in one cell. State the chromosome numbers of the four gametes made from that cell. (b) Suppose instead that meiosis I is normal, but in one of the two cells in meiosis II the two chromatids of chromosome 21 move to the same pole. State the chromosome numbers of the four gametes made from the original cell. (c) State the number of chromosomes in the zygote if a gamete with an extra chromosome 21 is fertilised by a normal sperm, and explain why that is.
H: Count 23 as the normal gamete. A gamete with an extra copy of one chromosome has 24 and one missing it has 22.
H: In (a) both cells made by meiosis I are abnormal; in (b) only one is.
A: (a) Both cells from meiosis I are abnormal: one has both chromosomes 21 and one has none. So two gametes have 24 chromosomes and two have 22. [B1] [B1]
(b) The cell that divided normally gives two normal gametes with 23 chromosomes. The other cell gives one gamete with 24 and one with 22. [B1] [B1]
(c) 24 + 23 = 47 chromosomes. [B1] The abnormal gamete supplies two copies of chromosome 21 and the normal sperm supplies one, so the zygote has three copies. [B1]
Q: [6 marks] ★★★ A horse has 2n = 64 and a donkey has 2n = 62. A mule, the offspring of a male donkey and a female horse, has 63 chromosomes and is usually sterile. (a) Calculate the number of chromosomes in a horse gamete and in a donkey gamete, and show that these give a mule with 63 chromosomes. (b) Use your knowledge of meiosis to suggest why a mule is usually sterile.
H: In prophase I, what must each chromosome do before the cell can continue meiosis normally?
A: (a) Horse gamete \(64 \div 2 = 32\) and donkey gamete \(62 \div 2 = 31\) chromosomes. [B1] The mule: \(32 + 31 = 63\). [B1]
(b) The mule has 63 chromosomes, an odd number, so they cannot all form homologous pairs. [B1]
The horse and donkey chromosomes are not all homologues of each other, so they cannot pair up properly in prophase I. [B1]
So the chromosomes are not distributed evenly in anaphase I, and gametes get unbalanced sets of chromosomes. [B1]
Few or no gametes are viable, so the mule is usually sterile. [B1]
:::

:::quiz
? A cell with 2n = 20 is in anaphase I of meiosis. How many chromosomes move towards each pole?
+ 10, each made of two chromatids
- 10, each made of one chromatid
- 20, each made of one chromatid
- 20, each made of two chromatids
> In anaphase I homologous chromosomes separate, so each pole gets one of each pair: 10 chromosomes, still with two chromatids each. Single chromatids moving apart belong to anaphase II or mitosis.
? During which stage do bivalents form?
+ prophase I
- metaphase II
- anaphase I
- prophase II
> Homologous chromosomes pair up as bivalents in prophase I, and the bivalents line up in metaphase I. There are no pairs in meiosis II.
? Which statement about crossing over is correct?
+ Non-sister chromatids exchange sections, forming new combinations of alleles.
- Sister chromatids exchange sections, forming new combinations of alleles.
- Whole chromosomes are exchanged between homologous pairs.
- It happens in prophase II and makes the cells diploid.
> Crossing over happens in prophase I between non-sister chromatids of a pair of homologues. Sister chromatids are identical, so swapping them changes nothing.
? A diploid cell has 2n = 14. What is the maximum number of combinations of chromosomes in gametes from random orientation, ignoring crossing over?
+ 128
- 14
- 49
- 7
> The haploid number is 7, so \(2^7 = 128\). Seven is the haploid number itself, 14 is the diploid number, and 49 is \(7^2\), which muddles the base and the power.
? In which stage of meiosis does the number of chromosomes per cell halve?
+ anaphase I (and telophase I)
- anaphase II
- prophase I
- fertilisation
> Whole chromosomes of each pair separate in meiosis I, so each cell has half the number. Meiosis II separates chromatids and leaves the number at n. Fertilisation doubles the number again.
? Which event at fertilisation increases genetic variation?
+ any sperm fuses with any egg, by chance
- the sperm and the egg fuse by mitosis
- the zygote divides by meiosis
- crossing over happens in the zygote
> Random fertilisation means the combination of the two gametes is a matter of chance. Meiosis makes the gametes, and the zygote divides by mitosis.
? Which feature is found in metaphase I but not in metaphase II?
+ chromosomes lined up in pairs on the equator
- chromosomes with two chromatids
- spindle fibres attached to centromeres
- no nuclear envelope
> In metaphase I bivalents line up as pairs. In metaphase II single chromosomes line up. The other three features appear in both.
? Which describes the cells produced by a complete meiosis in an animal?
+ four haploid cells, genetically different from each other
- two diploid cells, genetically identical to each other
- four diploid cells, genetically identical to each other
- two haploid cells, genetically different from each other
> Meiosis has two divisions, making four cells. They are haploid and, because of crossing over and random orientation, genetically different. Mitosis makes two identical diploid cells.
? The homologous chromosomes of a pair are best described as
+ chromosomes with the same genes at the same loci, one from each parent
- two identical copies of one chromosome joined at the centromere
- chromosomes with exactly the same alleles
- two chromosomes from the same parent
> A homologous pair has the same genes but may have different alleles, and one chromosome comes from each parent. Two identical copies joined at a centromere are sister chromatids.
:::

:::checklist What you can now do
- [ ] I can explain the meanings of haploid (n) and diploid (2n).
- [ ] I can explain what is meant by a homologous pair of chromosomes.
- [ ] I can explain why a reduction division is needed to make gametes.
- [ ] I can describe the behaviour of the chromosomes, nuclear envelope, cell surface membrane and spindle in each of the eight stages of meiosis.
- [ ] I can count chromosomes, chromatids and DNA molecules at each stage of meiosis.
- [ ] I can interpret diagrams and photomicrographs of cells in meiosis and identify the main stages.
- [ ] I can explain that crossing over and random orientation of homologous pairs and of chromatids produce genetically different gametes.
- [ ] I can explain that random fertilisation produces genetically different individuals.
- [ ] I can compare mitosis and meiosis.
:::

:::recap
- Diploid (2n) cells have two sets of chromosomes in homologous pairs; haploid (n) cells have one set. Human 2n = 46, n = 23.
- Homologous chromosomes carry the same genes at the same loci, but may have different alleles; sister chromatids are identical.
- Meiosis is a reduction division: one diploid nucleus makes four genetically different haploid nuclei, so fertilisation restores 2n.
- Meiosis I separates homologous chromosomes (pairing, crossing over, bivalents, no division of centromeres); meiosis II separates chromatids.
- The chromosome number halves in meiosis I; after meiosis II the cells have n chromosomes, each one chromatid.
- Identify stages: pairs mean meiosis I; whole chromosomes with two chromatids moving apart mean anaphase I; single chromatids moving apart mean anaphase II or mitosis.
- Crossing over: non-sister chromatids exchange sections in prophase I, making new allele combinations.
- Random orientation (independent assortment): \(2^n\) combinations for \(n\) pairs, \(2^{23} \approx 8.4\) million in humans; chromatids also orient at random in metaphase II.
- Random fertilisation: any gamete fuses with any other, so each zygote is different.
:::

:::links
- read: [CAIE A Level Biology: inherited change notes and topic questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/inherited-change/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Inheritance (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/16-inheritance/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of meiosis and crossing over
- read: [Meiosis and sexual reproduction](https://openstax.org/books/biology-2e/pages/11-introduction) · OpenStax Biology 2e · free university textbook chapter on meiosis, beyond the syllabus in places
- papers: [Paper 4 past papers](https://www.physicsandmathstutor.com/past-papers/a-level-biology/cie-paper-4/) · Physics & Maths Tutor · find the meiosis questions in real papers [unofficial]

Links checked 24 October 2026.
:::

Next: [Monohybrid inheritance](#bio.inheritance) uses the gametes that meiosis makes to predict the offspring of a cross.
