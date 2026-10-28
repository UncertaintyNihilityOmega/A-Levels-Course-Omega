@chapter bio.synthesis
@title Protein synthesis and gene mutation
@level as
@paper CAIE 9700 Papers 1 and 2
@time 4–5 hours
@summary A gene is a sequence of DNA bases that codes for a polypeptide. You will learn the features of the genetic code, how RNA polymerase makes messenger RNA in transcription, how a eukaryotic primary transcript is spliced, how ribosomes and transfer RNA build a polypeptide in translation, and how substitutions, insertions and deletions change the polypeptide made.

:::why
Every protein in your body, from the enzymes that digest your food to the haemoglobin that carries your oxygen, is made by reading a gene. The reading is the same in a bacterium, a plant and a human, which is why genes can be moved between species. When the sequence of a gene changes, the protein can change too, and that is the cause of many inherited diseases and the raw material of evolution. Exam questions give you a short DNA sequence and a code table and ask you to work out the mRNA, the polypeptide and the effect of a mutation, and they ask you to describe transcription and translation in the right words.
:::

**Before you start**, you should know the structure of DNA and mRNA and complementary base pairing from [Nucleic acids and DNA replication](#bio.dna), the primary structure of proteins from [Proteins](#bio.proteins), and ribosomes and the nucleus from [Eukaryotic cells and organelles](#bio.cells).

:::try Warm-up
Q: Write the base that pairs with each of A, T, C and G in DNA, and the base that pairs with A when mRNA is made. (from [Nucleic acids and DNA replication](#bio.dna))
A: A with T, T with A, C with G, G with C. When mRNA is made, A on the DNA template is paired with U (uracil), because RNA has no thymine.
Q: What is the primary structure of a protein, and which bond joins its amino acids? (from [Proteins](#bio.proteins))
A: The sequence of amino acids in the polypeptide chain. The amino acids are joined by peptide bonds.
Q: Name the organelle where polypeptides are made. (from [Eukaryotic cells and organelles](#bio.cells))
A: The ribosome (free in the cytoplasm or attached to the rough endoplasmic reticulum).
:::

## Genes and the genetic code

:::def Gene
A sequence of nucleotides, forming part of a DNA molecule, that codes for a polypeptide.
:::

Proteins are made of polypeptides, and the sequence of amino acids in a polypeptide decides its shape and its job (see [Proteins](#bio.proteins)). A gene holds the instructions for that sequence. The instructions are written in the order of the four bases (A, T, C and G) along one strand of DNA. The cell reads them in groups of three.

### Why three bases?

There are 20 different amino acids to code for. One base in a group gives only 4 possibilities. Two bases give \(4 \times 4 = 16\), which is not enough. Three bases give \(4 \times 4 \times 4 = 64\), which is enough for 20 amino acids and some signals. So the code uses **triplets**: groups of three bases.

:::def Genetic code
The set of rules by which the sequence of bases in DNA (and in mRNA) is translated into the sequence of amino acids in a polypeptide. Different triplets of bases either code for specific amino acids or correspond to start and stop codons.
:::

:::def Codon
A sequence of three bases on mRNA that codes for one amino acid, or is a start or stop signal.
:::

:::key Features of the genetic code
- **Triplet**: three bases code for one amino acid.
- **Degenerate**: most amino acids are coded for by more than one triplet (64 triplets, 20 amino acids).
- **Non-overlapping**: each base is part of only one triplet, and the bases are read in groups of three, one group after another.
- **Universal**: the same triplets code for the same amino acids in almost all organisms (bacteria, plants, animals and viruses).
- **Start and stop**: the codon **AUG** codes for methionine and is where translation starts. The codons **UAA, UAG and UGA** are stop codons: they code for no amino acid, and translation stops there.
:::

Here is the code for the **mRNA codons**. In the exam a table like this is printed in the question when you need it, so you do not learn it. Use it to look up each codon.

| amino acid | mRNA codons |
|---|---|
| alanine (Ala) | GCU GCC GCA GCG |
| arginine (Arg) | CGU CGC CGA CGG AGA AGG |
| asparagine (Asn) | AAU AAC |
| aspartic acid (Asp) | GAU GAC |
| cysteine (Cys) | UGU UGC |
| glutamic acid (Glu) | GAA GAG |
| glutamine (Gln) | CAA CAG |
| glycine (Gly) | GGU GGC GGA GGG |
| histidine (His) | CAU CAC |
| isoleucine (Ile) | AUU AUC AUA |
| leucine (Leu) | UUA UUG CUU CUC CUA CUG |
| lysine (Lys) | AAA AAG |
| methionine (Met) (start) | AUG |
| phenylalanine (Phe) | UUU UUC |
| proline (Pro) | CCU CCC CCA CCG |
| serine (Ser) | UCU UCC UCA UCG AGU AGC |
| threonine (Thr) | ACU ACC ACA ACG |
| tryptophan (Trp) | UGG |
| tyrosine (Tyr) | UAU UAC |
| valine (Val) | GUU GUC GUA GUG |
| stop | UAA UAG UGA |

Because there are 64 codons, 61 of them code for amino acids (**sense codons**) and 3 are stop codons.

:::warn Code, codon and amino acid sequence are different things
- The **sequence of amino acids** is the **result**, not the code.
- The **code** is the rule that links codons to amino acids.
- A **codon** is three bases on **mRNA**. An **anticodon** is three bases on **tRNA** (never on mRNA). The **triplet** on DNA is the template for a codon.
:::

## Transcription: making mRNA from DNA

DNA stays in the nucleus, but proteins are made in the cytoplasm at ribosomes. The cell copies the gene into a short molecule of mRNA that can leave the nucleus. Copying a gene into RNA is **transcription**.

:::def Transcription
The making of a molecule of messenger RNA by copying the base sequence of one strand of a gene in DNA, using the enzyme RNA polymerase.
:::

Only one of the two DNA strands is copied for any gene. This is the **transcribed strand**, also called the **template strand**. The other strand is the **non-transcribed strand**. The mRNA is complementary to the template strand, so it has the same sequence as the non-transcribed strand, except that U replaces T.

:::html
<figure class="fig small"><svg viewBox="0 0 352 248" role="img" aria-label="Transcription. RNA polymerase moves along the template strand of DNA, which is paired along the way with a growing strand of mRNA. The non-transcribed strand lies apart. The two DNA strands separate in front of the enzyme and rejoin behind it. The mRNA grows from its 5′ end and peels away from the template."><path class="f2 s-acc2 sw2" d="M242 90L241.5 95.7L240.1 101.4L237.7 106.8L234.5 112L230.4 116.8L225.6 121.1L220.1 124.9L214 128.1L207.4 130.7L200.5 132.5L193.3 133.6L186 134L178.7 133.6L171.5 132.5L164.6 130.7L158 128.1L151.9 124.9L146.4 121.1L141.6 116.8L137.5 112L134.3 106.8L131.9 101.4L130.5 95.7L130 90L130.5 84.3L131.9 78.6L134.3 73.2L137.5 68L141.6 63.2L146.4 58.9L151.9 55.1L158 51.9L164.6 49.3L171.5 47.5L178.7 46.4L186 46L193.3 46.4L200.5 47.5L207.4 49.3L214 51.9L220.1 55.1L225.6 58.9L230.4 63.2L234.5 68L237.7 73.2L240.1 78.6L241.5 84.3Z"/><path class="c1 sw3" d="M28 92L324 92"/><path class="c3 sw3" d="M28 60L92 60L108 34L246 34L262 60L324 60"/><path class="ln-m thin" d="M34 63L34 89"/><path class="ln-m thin" d="M46 63L46 89"/><path class="ln-m thin" d="M58 63L58 89"/><path class="ln-m thin" d="M70 63L70 89"/><path class="ln-m thin" d="M82 63L82 89"/><path class="ln-m thin" d="M268 63L268 89"/><path class="ln-m thin" d="M280 63L280 89"/><path class="ln-m thin" d="M292 63L292 89"/><path class="ln-m thin" d="M304 63L304 89"/><path class="ln-m thin" d="M316 63L316 89"/><path class="c2 sw3" d="M144 116L226 116"/><path class="ln-m thin" d="M152 96L152 112"/><path class="ln-m thin" d="M164 96L164 112"/><path class="ln-m thin" d="M176 96L176 112"/><path class="ln-m thin" d="M188 96L188 112"/><path class="ln-m thin" d="M200 96L200 112"/><path class="ln-m thin" d="M212 96L212 112"/><path class="ln-m thin" d="M224 96L224 112"/><path class="c2 sw3" d="M144 116L122 150L28 150"/><text class="tl tb" x="186" y="66" text-anchor="middle">RNA</text><text class="tl tb" x="186" y="81" text-anchor="middle">polymerase</text><circle class="f1 s-acc sw2" cx="272" cy="130" r="6"/><circle class="f1 s-acc sw2" cx="294" cy="118" r="6"/><text class="tl" x="8" y="96">3′</text><text class="tl" x="330" y="96">5′</text><text class="tl" x="8" y="154">5′</text><text class="tl" x="248" y="121">3′</text><text class="tl" x="10" y="18">non-transcribed strand</text><path class="ln-m thin" d="M40 22L40 57"/><text class="tl" x="8" y="126">template strand</text><path class="ln-m thin" d="M50 112L50 96"/><text class="tl" x="36" y="170">mRNA</text><text class="tl" x="236" y="166">free RNA</text><text class="tl" x="236" y="180">nucleotides</text><path class="ln-m thin" d="M262 152L270 137"/><path class="ln" d="M110 214L290 214" marker-end="url(#ah)"/><text class="tl" x="110" y="236">direction of transcription</text></svg><figcaption>Transcription (simplified). RNA polymerase separates the two DNA strands over a short stretch, builds mRNA by pairing free RNA nucleotides with the template strand, and moves on. The mRNA is made 5′ to 3′ and leaves the template. Only the template strand is copied.</figcaption></figure>
:::

:::steps
1. **RNA polymerase** attaches to the DNA at the start of the gene. The hydrogen bonds between the bases break and the two strands separate over a short stretch.
2. Free **RNA nucleotides** pair with the bases of the **template strand** by complementary base pairing: A with U, T with A, C with G and G with C.
3. RNA polymerase moves along the template strand and joins the RNA nucleotides by **phosphodiester bonds**, building the mRNA in the **5′ to 3′** direction.
4. At the end of the gene, RNA polymerase and the new mRNA come off the DNA. The DNA strands rejoin and the double helix re-forms behind the enzyme.
5. The mRNA leaves the nucleus through a **nuclear pore** and goes to a ribosome.
:::

:::def RNA polymerase
An enzyme that joins RNA nucleotides, using a template strand of DNA, to make a molecule of RNA. It forms phosphodiester bonds between the nucleotides.
:::

:::warn Do not mix up the two polymerases
**DNA polymerase** copies a whole DNA molecule in S phase, using both strands, and uses DNA nucleotides (with T). **RNA polymerase** copies only one strand of one gene, uses RNA nucleotides (with U), and makes a single strand.
:::

:::eg Describe how mRNA is made from a gene by transcription.
Five marking points, in order.

RNA polymerase attaches to the DNA, and the hydrogen bonds between the two strands break, so the strands separate at the gene. [B1]

Only one strand, the template (transcribed) strand, is copied. [B1]

Free RNA nucleotides pair with the exposed bases of the template strand by complementary base pairing (A with U, C with G). [B1]

RNA polymerase joins the RNA nucleotides by phosphodiester bonds, making mRNA in the 5′ to 3′ direction. [B1]

The mRNA leaves the DNA and passes out of the nucleus through a nuclear pore; the DNA strands rejoin. [B1]

A weaker answer says "the DNA is copied into RNA". It does not say that only one strand is used, mentions no RNA polymerase or base pairing, and so gets one mark at most.
:::

### Eukaryotic genes: introns and exons

In a bacterium the mRNA is ready to use as soon as it is made. In a **eukaryote**, the RNA made by transcription is a first copy of the whole gene, called the **primary transcript**. It contains two kinds of sequence.

:::def Exon
A sequence in a gene, and in its primary transcript, that codes for part of the polypeptide. Exons are kept in the mRNA.
:::

:::def Intron
A non-coding sequence in a gene, and in its primary transcript, that lies between exons. Introns are removed from the primary transcript.
:::

In the nucleus, the introns are cut out and the exons are joined together to make the mRNA. This is **splicing**. The mRNA is shorter than the gene, and only the mRNA goes to the cytoplasm.

:::html
<figure class="fig small"><svg viewBox="0 0 346 262" role="img" aria-label="Splicing. The primary transcript has four exons, numbered 1 to 4, separated by three introns drawn as thin lines. The introns are removed and the four exons are joined end to end to make the shorter mRNA."><text class="tl tb" x="16" y="20">primary transcript (copy of the gene)</text><path class="ln thick" d="M22 60L312 60"/><rect class="f2 s-acc2 sw2" x="22" y="48" width="50" height="24"/><text class="tl tb" x="47" y="65" text-anchor="middle">1</text><rect class="f2 s-acc2 sw2" x="104" y="48" width="40" height="24"/><text class="tl tb" x="124" y="65" text-anchor="middle">2</text><rect class="f2 s-acc2 sw2" x="176" y="48" width="60" height="24"/><text class="tl tb" x="206" y="65" text-anchor="middle">3</text><rect class="f2 s-acc2 sw2" x="268" y="48" width="30" height="24"/><text class="tl tb" x="283" y="65" text-anchor="middle">4</text><text class="tl" x="4" y="86">5′</text><text class="tl" x="324" y="64">3′</text><text class="tl" x="40" y="112">exon (kept)</text><path class="ln-m thin" d="M50 98L50 74"/><text class="tl" x="140" y="112">intron (removed)</text><path class="ln-m thin" d="M160 98L160 62"/><path class="ln" d="M165 130L165 190" marker-end="url(#ah)"/><text class="tl" x="176" y="150">splicing: introns</text><text class="tl" x="176" y="164">removed, exons joined</text><text class="tl tb" x="16" y="214">mRNA</text><rect class="f2 s-acc2 sw2" x="22" y="224" width="50" height="24"/><text class="tl tb" x="47" y="241" text-anchor="middle">1</text><rect class="f2 s-acc2 sw2" x="72" y="224" width="40" height="24"/><text class="tl tb" x="92" y="241" text-anchor="middle">2</text><rect class="f2 s-acc2 sw2" x="112" y="224" width="60" height="24"/><text class="tl tb" x="142" y="241" text-anchor="middle">3</text><rect class="f2 s-acc2 sw2" x="172" y="224" width="30" height="24"/><text class="tl tb" x="187" y="241" text-anchor="middle">4</text></svg><figcaption>Splicing in the nucleus (simplified). The primary transcript is a copy of the whole gene. The introns (non-coding) are cut out and the exons (coding) are joined to make the mRNA, which is shorter than the gene.</figcaption></figure>
:::

:::eg A eukaryotic gene has four exons, of 150, 210, 330 and 210 bases, and three introns, of 420, 800 and 560 bases. All the exons code for the polypeptide, including the stop codon. Calculate the length of the primary transcript, the length of the mRNA and the number of amino acids in the polypeptide.
**Step 1: primary transcript.** It is a copy of the whole gene, so add every exon and every intron:

\[\begin{aligned} \text{exons} &= 150 + 210 + 330 + 210 = 900 \\ \text{introns} &= 420 + 800 + 560 = 1780 \\ \text{primary transcript} &= 900 + 1780 = 2680\ \text{bases} \end{aligned}\]

**Step 2: mRNA.** The introns are removed, so the mRNA is the exons joined: 900 bases. [M1] [A1]

**Step 3: amino acids.** There are \(900 \div 3 = 300\) codons. One of them is the stop codon, which codes for no amino acid, so the polypeptide has \(300 - 1 = 299\) amino acids. [M1] [A1]
:::

## Translation: making a polypeptide

Translation is the stage in which the sequence of codons in mRNA is turned into a sequence of amino acids, at a ribosome.

:::def Translation
The assembly of amino acids into a polypeptide at a ribosome, in the order that is specified by the codons of mRNA.
:::

Three kinds of RNA take part (you do not need to know a third kind, ribosomal RNA, which is part of the ribosome):
- **mRNA** carries the codons.
- **tRNA** (transfer RNA) brings amino acids to the ribosome. 
- The **ribosome** holds the mRNA and the tRNA molecules in place while the amino acids are joined.

:::def Transfer RNA (tRNA)
A single polynucleotide strand of RNA, folded into a clover-leaf shape, with an anticodon of three bases at one end and a site that binds one specific amino acid at the other.
:::

:::def Anticodon
A sequence of three bases on a tRNA molecule that is complementary to a codon on mRNA, and pairs with it by hydrogen bonds.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 350 284" role="img" aria-label="A tRNA molecule, drawn as a clover-leaf with a stem. The amino acid methionine is attached at the top of the stem. At the bottom, the anticodon U A C pairs by hydrogen bonds with the codon A U G on an mRNA strand."><rect class="fm s-acc sw2" x="140" y="40" width="20" height="130"/><circle class="fm s-acc sw2" cx="116" cy="112" r="27"/><circle class="fm s-acc sw2" cx="184" cy="112" r="27"/><circle class="fm s-acc sw2" cx="150" cy="188" r="32"/><rect class="fm" x="141" y="41" width="18" height="122"/><circle class="f1 s-acc sw2" cx="150" cy="24" r="15"/><text class="tl tb" x="150" y="29" text-anchor="middle">Met</text><text class="tl tb" x="128" y="193" text-anchor="middle">U</text><path class="ln-m thin dash" d="M128 224L128 244"/><text class="tl tb" x="150" y="193" text-anchor="middle">A</text><path class="ln-m thin dash" d="M150 224L150 244"/><text class="tl tb" x="172" y="193" text-anchor="middle">C</text><path class="ln-m thin dash" d="M172 224L172 244"/><text class="tl tb" x="128" y="262" text-anchor="middle">A</text><text class="tl tb" x="150" y="262" text-anchor="middle">U</text><text class="tl tb" x="172" y="262" text-anchor="middle">G</text><path class="c2 sw3" d="M100 270L200 270"/><text class="tl" x="186" y="28">amino acid (here Met)</text><path class="ln-m thin" d="M182 26L166 26"/><text class="tl tb" x="10" y="116">tRNA</text><text class="tl" x="224" y="194">anticodon</text><path class="ln-m thin" d="M220 190L186 190"/><text class="tl" x="224" y="238">hydrogen bonds</text><path class="ln-m thin" d="M220 234L178 234"/><text class="tl" x="224" y="266">codon on mRNA</text><path class="ln-m thin" d="M220 262L206 262"/></svg><figcaption>A transfer RNA molecule (simplified). One end carries a specific amino acid. The anticodon at the other end is three bases that are complementary to a codon on mRNA, and it pairs with that codon by hydrogen bonds.</figcaption></figure>
:::

Each kind of tRNA carries one kind of amino acid, and its anticodon matches the codon for that amino acid. (An enzyme attaches each amino acid to the right tRNA, using energy from ATP.)

:::steps
1. A ribosome attaches to the **mRNA** at the **start codon**, AUG.
2. A **tRNA** with the **anticodon** UAC, carrying the amino acid methionine, pairs with the start codon by **complementary base pairing** (hydrogen bonds).
3. A second tRNA, carrying the amino acid that the next codon codes for, pairs with the next codon. The ribosome holds two tRNA molecules at a time.
4. A **peptide bond** forms between the two amino acids, in a condensation reaction. The first tRNA, now free of its amino acid, leaves and picks up another amino acid.
5. The ribosome moves along the mRNA by **one codon** (in the 5′ to 3′ direction). The next tRNA pairs with the next codon and its amino acid is joined to the chain. This repeats, and the polypeptide grows.
6. At a **stop codon** (UAA, UAG or UGA) there is no tRNA with a matching anticodon. The polypeptide is released and the ribosome comes off the mRNA.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 350 320" role="img" aria-label="Translation at a ribosome. The mRNA runs between the large and small subunits. Two tRNA molecules, with anticodons GGU and CUU, are paired by hydrogen bonds with the codons CCA and GAA. The first tRNA carries the growing polypeptide, Met then Pro, and the second tRNA carries glutamic acid. A new peptide bond forms between them. The ribosome moves one codon to the right."><path class="c2 sw3" d="M22 210L330 210"/><rect class="fp ln" x="54" y="198" width="64" height="24"/><text class="tl tb" x="72" y="215" text-anchor="middle">C</text><text class="tl tb" x="86" y="215" text-anchor="middle">C</text><text class="tl tb" x="100" y="215" text-anchor="middle">A</text><rect class="fp ln" x="122" y="198" width="64" height="24"/><text class="tl tb" x="140" y="215" text-anchor="middle">G</text><text class="tl tb" x="154" y="215" text-anchor="middle">A</text><text class="tl tb" x="168" y="215" text-anchor="middle">A</text><rect class="fp ln" x="190" y="198" width="64" height="24"/><text class="tl tb" x="208" y="215" text-anchor="middle">U</text><text class="tl tb" x="222" y="215" text-anchor="middle">U</text><text class="tl tb" x="236" y="215" text-anchor="middle">U</text><rect class="fm s-acc sw2" x="40" y="44" width="160" height="120" rx="26"/><rect class="fm2 s-acc sw2" x="52" y="236" width="140" height="24" rx="12"/><rect class="f2 s-acc2 sw2" x="62" y="98" width="48" height="54" rx="8"/><text class="tl tb" x="72" y="144" text-anchor="middle">G</text><path class="ln-m thin dash" d="M72 172L72 194"/><text class="tl tb" x="86" y="144" text-anchor="middle">G</text><path class="ln-m thin dash" d="M86 172L86 194"/><text class="tl tb" x="100" y="144" text-anchor="middle">U</text><path class="ln-m thin dash" d="M100 172L100 194"/><circle class="f1 s-acc sw2" cx="86" cy="80" r="13"/><text class="tl tb" x="86" y="85" text-anchor="middle">Pro</text><rect class="f2 s-acc2 sw2" x="130" y="98" width="48" height="54" rx="8"/><text class="tl tb" x="140" y="144" text-anchor="middle">C</text><path class="ln-m thin dash" d="M140 172L140 194"/><text class="tl tb" x="154" y="144" text-anchor="middle">U</text><path class="ln-m thin dash" d="M154 172L154 194"/><text class="tl tb" x="168" y="144" text-anchor="middle">U</text><path class="ln-m thin dash" d="M168 172L168 194"/><circle class="f1 s-acc sw2" cx="154" cy="80" r="13"/><text class="tl tb" x="154" y="85" text-anchor="middle">Glu</text><circle class="f1 s-acc sw2" cx="66" cy="58" r="13"/><text class="tl tb" x="66" y="63" text-anchor="middle">Met</text><path class="ln thick" d="M72 69L78 68"/><path class="ln dash" d="M100 80L140 80"/><text class="tl" x="4" y="214">5′</text><text class="tl" x="334" y="214">3′</text><text class="tl" x="4" y="16">growing</text><text class="tl" x="4" y="30">polypeptide</text><path class="ln-m thin" d="M62 33L60 47"/><text class="tl" x="150" y="16">new peptide bond</text><path class="ln-m thin" d="M196 22L120 76"/><text class="tl" x="212" y="70">large subunit</text><path class="ln-m thin" d="M208 66L198 70"/><text class="tl" x="212" y="100">amino acid</text><path class="ln-m thin" d="M208 96L169 82"/><text class="tl" x="212" y="130">tRNA</text><path class="ln-m thin" d="M208 126L178 126"/><text class="tl" x="212" y="158">anticodon</text><path class="ln-m thin" d="M208 154L172 146"/><text class="tl" x="260" y="186">codon</text><path class="ln-m thin" d="M256 188L238 200"/><text class="tl" x="212" y="252">small subunit</text><path class="ln-m thin" d="M208 248L194 248"/><path class="ln" d="M54 288L190 288" marker-end="url(#ah)"/><text class="tl" x="16" y="308">ribosome moves 5′ → 3′</text></svg><figcaption>Translation (simplified). The ribosome holds two tRNA molecules at a time. Each anticodon pairs with a codon on the mRNA. A peptide bond joins the amino acid on the second tRNA to the growing chain, the first tRNA leaves, and the ribosome moves along by one codon.</figcaption></figure>
:::

Translation uses energy from ATP. Many ribosomes can translate the same mRNA at the same time, so many copies of the polypeptide are made from one mRNA molecule.

:::key From DNA to polypeptide in one chain
DNA template triplet → mRNA codon → tRNA anticodon → amino acid. For example: template **TAC** → codon **AUG** → anticodon **UAC** → **methionine**.
:::

:::eg A template strand of DNA reads 3′–TACGGTCTTAAACCCATC–5′. Use the table of mRNA codons above to find the mRNA sequence, the anticodon for the third codon, and the amino acids.
**Step 1: transcribe.** Replace each base by its partner (A is paired with U in RNA, not T), and write the mRNA in the 5′ to 3′ direction (left to right, because the template is written 3′ to 5′):

\[\begin{aligned} &3′\text{–TAC GGT CTT AAA CCC ATC–}5′ \\ &5′\text{–AUG CCA GAA UUU GGG UAG–}3′ \end{aligned}\]

[M1] [A1]

**Step 2: anticodon for the third codon.** The third codon is GAA, so the anticodon is its complement, CUU. [A1]

**Step 3: translate.** Look up each codon: AUG is Met, CCA is Pro, GAA is Glu, UUU is Phe, GGG is Gly and UAG is a stop codon. The polypeptide is Met–Pro–Glu–Phe–Gly. [A1]
:::

:::exam Describe translation in the right order
A six-mark question on translation wants: the ribosome and mRNA; tRNA with a complementary **anticodon** pairing with a **codon**; the amino acid each tRNA carries; the **peptide bond**; the ribosome moving along the mRNA; the **stop codon**. Use "codon" for mRNA and "anticodon" for tRNA.
:::

:::eg Describe how a polypeptide is made at a ribosome from mRNA.
Six marking points, in order.

The mRNA binds to the ribosome, which begins at a start codon (AUG). [B1]

A tRNA molecule with a complementary anticodon pairs with a codon on the mRNA by hydrogen bonds. [B1]

Each tRNA carries a specific amino acid, so the order of codons decides the order of amino acids. [B1]

The ribosome holds two tRNA molecules at a time, and a peptide bond forms between their amino acids. [B1]

The ribosome moves along the mRNA one codon at a time, and the free tRNA leaves. [B1]

This continues until a stop codon is reached, when the polypeptide is released. [B1]

A weaker answer says "the tRNA reads the codons and the amino acids join up". It never names the anticodon, the peptide bond or the stop codon.
:::

Try it: in the tool below the strand of DNA you see is the template, and the mRNA, the tRNA anticodons and the amino acids are worked out from it, using the same code table as above. Type your own template strand, or use the tabs to see what happens to the polypeptide when a mutation is made (the next section explains each kind).

:::html
<div class="widget" data-w="bio-codon" data-dna="TACCGAAAGTTTCCGATT" data-mutate="none"></div>
:::

## Gene mutations

:::def Gene mutation
A change in the sequence of base pairs in a DNA molecule that may result in an altered polypeptide.
:::

A gene mutation can happen when DNA is copied (an error that is not corrected) or when DNA is damaged by radiation or chemicals. If the change is in a body cell it is not passed on to offspring; if it is in a cell that makes gametes it can be inherited. A mutation changes a gene, but what it does to the polypeptide depends on what kind of mutation it is, and where.

:::key Three kinds of gene mutation
1. **Substitution**: one nucleotide is replaced by a different one.
2. **Insertion**: one or more extra nucleotides are added to the sequence.
3. **Deletion**: one or more nucleotides are removed from the sequence.
:::

### Substitution

Replacing one base changes only one codon, so at most one amino acid changes. There are three possible results.

- **Silent mutation.** The new codon codes for the **same** amino acid, because the genetic code is degenerate. The polypeptide is unchanged. (For example GAA and GAG both code for glutamic acid.)
- **Missense mutation.** The new codon codes for a **different** amino acid. The polypeptide has one amino acid changed. It may work normally, or the change in R group may alter the bonds that hold the tertiary structure (see [Proteins](#bio.proteins)), so that the protein works less well or not at all.
- **Nonsense mutation.** The new codon is a **stop codon**. Translation stops early, so the polypeptide is shorter and usually does not work.

:::eg The table shows five changes to the mRNA 5′–AUG CCA GAA UUU GGG UAG–3′, which codes for Met–Pro–Glu–Phe–Gly. Describe the effect of each change on the polypeptide.
| change | new mRNA | new polypeptide |
|---|---|---|
| CCA to CCG (substitution) | AUG CCG GAA UUU GGG UAG | Met–Pro–Glu–Phe–Gly |
| GAA to GAC (substitution) | AUG CCA GAC UUU GGG UAG | Met–Pro–Asp–Phe–Gly |
| GAA to UAA (substitution) | AUG CCA UAA UUU GGG UAG | Met–Pro |
| U inserted after AUG | AUG UCC AGA AUU UGG GUA G | Met–Ser–Arg–Ile–Trp–Val |
| 3 bases (CCA) deleted | AUG GAA UUU GGG UAG | Met–Glu–Phe–Gly |

The first substitution is silent: both CCA and CCG code for proline, so the polypeptide does not change. [B1]

The second is a missense mutation: aspartic acid replaces glutamic acid, so one amino acid is changed. [B1]

The third is a nonsense mutation: UAA is a stop codon, so translation stops after two amino acids and the polypeptide is shorter. [B1]

The insertion is a frameshift: every codon after the change is different, so every amino acid after methionine changes. [B1]

The deletion of three bases removes one codon and keeps the reading frame, so only one amino acid (Pro) is lost and the others are unchanged. [B1]
:::

### Insertion and deletion: the reading frame

The mRNA is read in groups of three from the start codon. If one base is inserted or deleted, **every codon after that point is read in a different grouping**. This is called a **frameshift**. All the amino acids after the mutation are changed, and the change often creates a stop codon, so the polypeptide is usually very different and does not work.

:::key Insertions and deletions
- Insert or delete **1 or 2 bases** (not a multiple of 3): frameshift. Every amino acid after the change is affected.
- Insert or delete **3 bases** (or a multiple of 3): the frame is kept. One amino acid (or a few) is added or lost and the rest is unchanged.
- A substitution never causes a frameshift, because the number of bases is the same.
:::

:::warn Not every deletion of three bases is a frameshift, and not every mutation is harmful
- A deletion of three bases removes one codon and keeps the frame, so the rest of the polypeptide is unchanged (unless the deletion makes a new stop codon).
- Mutations can be **harmful, neutral or (rarely) beneficial**. Silent mutations have no effect, and some missense mutations help an organism to survive in a new environment.
- A mutation changes the **DNA**: it is the polypeptide that is altered, not the "code".
:::

Try it: this time the tool starts with a mutation already made. Use the tabs to change its type, and the slider to move its position along the sequence. Notice which changes alter only one amino acid and which alter every amino acid after the change.

:::html
<div class="widget" data-w="bio-codon" data-dna="TACCGAAAGTTTCCGATT" data-mutate="sub" data-pos="4"></div>
:::

:::eg Real context, sickle cell anaemia: haemoglobin carries oxygen in red blood cells. In the gene for one of its polypeptides, the template triplet CTC is changed to CAC. Use the code table to find the effect, and explain why one change can make red blood cells abnormal.
The template triplet CTC is transcribed to the mRNA codon GAG, which codes for glutamic acid. [B1]

The template triplet CAC is transcribed to GUG, which codes for valine. [B1]

This is a substitution (one base is replaced). It is a missense mutation, because one amino acid is changed, from glutamic acid to valine. [B1]

The R group of valine is different from that of glutamic acid, so the tertiary structure and the way haemoglobin molecules interact change, and the red blood cells can become abnormal. [B1]

(The full explanation of sickle cell anaemia is in the A Level chapters. At this level you need the chain: one base changed, one amino acid changed, a different R group, a changed protein.)
:::

:::eg Real context, an inherited disease: in a patient with an inherited disease, the gene for an enzyme has a mutation. The normal polypeptide has 300 amino acids. In the patient, the mRNA has a stop codon where codon 120 should be. Explain why the patient's enzyme does not work.
The mutation is a nonsense mutation: a substitution has changed the codon into a stop codon (UAA, UAG or UGA). [B1]

Translation stops at codon 120, so the polypeptide has only 119 amino acids instead of 300. [B1]

The shorter chain cannot fold to give the correct tertiary structure and active site, so the substrate is not complementary and the enzyme does not work. [B1]
:::

:::eg Spot the error: describe how a tRNA molecule takes part in translation. [3]
A student wrote this answer.

Line 1: The tRNA carries a codon that pairs with the anticodon on the mRNA.
Line 2: The tRNA carries a specific amino acid.
Line 3: The amino acid is joined to the polypeptide chain by a peptide bond, and the tRNA then leaves the ribosome.

**Line 1 is wrong: the mRNA carries the codon and the tRNA carries the anticodon, which pairs with the codon. That mark is lost [B0].** Line 2 is correct [B1]. Line 3 is correct [B1].

Correct Line 1: "The tRNA has an anticodon that pairs with a codon on the mRNA." With that change the answer scores 3 marks.
:::

## Practice

:::try Start easy, finish at exam standard
Q: State the number of bases in a codon, and calculate the number of different codons that are possible.
A: Three bases. \(4 \times 4 \times 4 = 64\) possible codons.
Q: Explain why a code of two bases per amino acid could not code for 20 amino acids.
A: Two bases give only \(4 \times 4 = 16\) different combinations, which is fewer than the 20 amino acids.
Q: The template strand of a gene reads 3′–TACGGCTTTATT–5′. Write the mRNA, and give the anticodon of the second codon.
A: mRNA: 5′–AUG CCG AAA UAA–3′. The second codon is CCG, so its anticodon is GGC.
Q: Use the code table to translate the mRNA 5′–AUG UGG CAU UAA–3′.
A: AUG is Met, UGG is Trp, CAU is His and UAA is a stop codon. The polypeptide is Met–Trp–His.
Q: A polypeptide has 120 amino acids. Calculate the least number of bases in the mRNA that is translated, including the start and stop codons.
A: 120 amino acids need 120 codons, plus one stop codon: \(121 \times 3 = 363\) bases (the start codon codes for the first amino acid).
Q: State two ways in which tRNA differs from mRNA.
A: tRNA is folded into a clover-leaf shape (mRNA is a straight strand). tRNA has an anticodon and an amino-acid binding site (mRNA has codons). tRNA is shorter and carries amino acids to the ribosome (mRNA carries the code).
Q: State what is meant by the template strand and the non-transcribed strand.
A: The template (transcribed) strand is the strand of DNA that is copied to make mRNA. The non-transcribed strand is the other strand of the gene, which is not copied.
Q: A eukaryotic gene is 2500 bases long. The mRNA made from it is 1200 bases long. Explain the difference, and calculate the total length of the introns.
A: The primary transcript is a copy of the whole gene. Introns (non-coding sequences) are removed and the exons are joined to make the mRNA, so the mRNA is shorter. \(2500 - 1200 = 1300\) bases of introns (assuming all the mRNA is exons).
Q: A substitution changes the mRNA codon GAA to GAG. Name the type of mutation and explain the effect on the polypeptide.
A: A silent mutation. GAA and GAG both code for glutamic acid (the code is degenerate), so the polypeptide is unchanged.
Q: Explain why translation stops at a stop codon.
A: No tRNA has an anticodon that is complementary to a stop codon, so no amino acid is added. The polypeptide is released from the ribosome.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ State what is meant by (a) a gene and (b) a codon.
A: (a) A gene is a sequence of nucleotides, forming part of a DNA molecule, that codes for a polypeptide. [B1]
(b) A codon is a sequence of three bases on mRNA that codes for one amino acid (or is a start or stop signal). [B1]
Q: [4 marks] ★★ The template strand of a short gene reads 3′–TACAAGGGCGAAACT–5′. The mRNA codons AUG, UUC, CCG and CUU code for methionine, phenylalanine, proline and leucine, and UGA is a stop codon. (a) Write the sequence of the mRNA. (b) Write the anticodon of the tRNA that pairs with the second codon. (c) Give the amino acids in the polypeptide.
H: Replace each base by its partner. In RNA, A is paired with U.
H: The anticodon is complementary to the codon.
A: (a) 5′–AUG UUC CCG CUU UGA–3′ [B1]
(b) The second codon is UUC, so the anticodon is AAG. [B1]
(c) Methionine–phenylalanine–proline–leucine [B1]
translation stops at the stop codon UGA, which codes for no amino acid. [B1]
Q: [4 marks] ★★ A gene codes for the mRNA 5′–AUG GAA CUU AAA UUU GGC UGA–3′, which codes for Met–Glu–Leu–Lys–Phe–Gly. Three mutant genes were found. In mutant 1, GAA changed to GAG. In mutant 2, AAA changed to UAA. In mutant 3, the first U of UUU was deleted. Give the polypeptide for each mutant and name the type of mutation.
H: Write out the mutant mRNA and read it in groups of three from AUG.
H: Mutant 3: after the deletion, the bases after the deleted one shift along.
A: Mutant 1: Met–Glu–Leu–Lys–Phe–Gly (unchanged); a silent mutation, because the code is degenerate (GAG also codes for glutamic acid). [B1] [B1]
Mutant 2: Met–Glu–Leu; a nonsense mutation, because UAA is a stop codon, so the polypeptide is shorter. [B1]
Mutant 3: Met–Glu–Leu–Lys–Leu–Ala, with every amino acid after the deletion changed; a frameshift (deletion) mutation. [B1]
Q: [6 marks] ★★ Describe how a ribosome makes a polypeptide using the information in a molecule of mRNA.
H: Start with the mRNA and the start codon, and finish with the stop codon.
H: Use the words codon, anticodon and peptide bond.
A: The mRNA binds to the ribosome and translation starts at the start codon, AUG. [B1]
A tRNA molecule with a complementary anticodon pairs with the codon by hydrogen bonds. [B1]
Each tRNA carries a specific amino acid, so the order of codons decides the order of amino acids. [B1]
A peptide bond forms between the amino acids on two adjacent tRNA molecules. [B1]
The ribosome moves along the mRNA one codon at a time and the free tRNA leaves. [B1]
At a stop codon the polypeptide is released. [B1]
Q: [5 marks] ★★ A eukaryotic gene has three exons, of 114, 180 and 150 bases, separated by two introns, of 340 and 610 bases. (a) Calculate the length of the primary transcript. (b) The three exons all code for the polypeptide, including the stop codon. Calculate the number of amino acids in the polypeptide. (c) Describe how the primary transcript is changed to form mRNA.
H: The primary transcript is a copy of the whole gene.
H: Each amino acid needs one codon, and the stop codon needs one as well.
A: (a) \(114 + 180 + 150 + 340 + 610 = 1394\) bases [B1]
(b) \((114 + 180 + 150) \div 3 = 148\) codons [M1], so \(148 - 1 = 147\) amino acids [A1]
(c) The introns (non-coding sequences) are removed. [B1]
The exons (coding sequences) are joined together to make the mRNA. [B1]
Q: [6 marks] (#bio.enzymes) ★★★ A gene codes for an enzyme. In one mutant, a substitution changes an amino acid in the active site to one with a different R group. In a second mutant, a substitution changes the codon to another codon for the same amino acid. In a third mutant, one base is deleted near the start of the gene. (a) Explain why the first mutant has a lower activity. (b) Explain why the second mutant has normal activity. (c) Explain why the third mutant has no activity.
H: What does the R group of an amino acid decide about the active site?
H: For (c), what happens to every codon after a deletion?
A: (a) The different R group forms different bonds, so the tertiary structure changes, and the shape of the active site changes. [B1]
The substrate is less complementary to the active site, so fewer enzyme–substrate complexes form. [B1]
(b) The genetic code is degenerate, so the same amino acid is coded for and the polypeptide is unchanged. [B1]
(c) The deletion causes a frameshift: every codon after the deletion is read differently, so the amino acids after it are changed. [B1]
The polypeptide folds into a different tertiary structure (or is stopped early by a new stop codon), so the active site is lost. [B1]
Without an active site, the enzyme cannot bind its substrate or catalyse the reaction. [B1]
Q: [5 marks] ★★ A gene for a polypeptide of 250 amino acids was altered in four mutants. The table shows the length of the polypeptide made.

| mutant | change to the gene | polypeptide length / amino acids |
|---|---|---|
| 1 | one substitution | 250 |
| 2 | one substitution | 79 |
| 3 | three bases deleted | 249 |
| 4 | one base deleted | 61 |

(a) Explain the result for mutant 2. (b) Explain why mutant 3 makes a polypeptide that is only one amino acid shorter. (c) Suggest why mutant 4 makes a much shorter polypeptide than mutant 3.
H: A substitution cannot change the number of bases. How can it change the length?
H: Does a deletion of three bases keep the reading frame?
A: (a) The substitution changed the codon for amino acid 80 into a stop codon (a nonsense mutation). [B1]
Translation stopped at that codon, so only 79 amino acids were made. [B1]
(b) Deleting three bases removes one codon and keeps the reading frame, so one amino acid is lost and the rest of the sequence is unchanged. [B1]
(c) Deleting one base causes a frameshift, so every codon after the deletion is read differently. [B1]
By chance a new stop codon appeared, so translation stopped early. [B1]
Q: [5 marks] (#bio.dna) ★★★ A base on one strand of a DNA molecule is changed to a different base just before S phase. The cell then divides by mitosis. Explain why only one of the two daughter cells has the mutation in its DNA.
H: Each strand of the DNA is used as a template. What base is paired with the changed base?
H: Semi-conservative replication gives each new molecule one old strand.
A: DNA replication is semi-conservative: each strand is a template for a new strand. [B1]
The strand with the changed base is used as a template, so the new strand has a base that pairs with the changed base. [B1]
This DNA molecule has the mutation in both its strands. [B1]
The other original strand is unchanged, so it is copied into a DNA molecule with no mutation. [B1]
In mitosis, each daughter cell receives one of the two DNA molecules, so only one cell has the mutation. [B1]
:::

:::try Stretch for A*
Q: [6 marks] ★★★ A mRNA reads 5′–AUG ACC GGA UUC CAU GAA UUU CAG UAG–3′. Use the code table above. (a) Give the polypeptide that it codes for. (b) One A is inserted between the first and second codons (after AUG). Give the polypeptide and explain the change. (c) A second mutation then deletes one G from GGA in the mutated sequence. Give the polypeptide that is made from the mRNA with both mutations, and explain why it differs from the original in only two amino acids.
H: For (b), write the new sequence and read it in groups of three. Which codon will appear in the middle?
H: For (c), after the deletion, do the bases line up in the original groups again?
A: (a) Met–Thr–Gly–Phe–His–Glu–Phe–Gln [B1]
(b) AUG AAC CGG AUU CCA UGA: Met–Asn–Arg–Ile–Pro [B1]
The insertion is a frameshift, so every codon after it is read differently, and a stop codon (UGA) appears early, so the polypeptide is shorter. [B1]
(c) AUG AAC CGA UUC CAU GAA UUU CAG UAG: Met–Asn–Arg–Phe–His–Glu–Phe–Gln [B1]
The deletion removes one base after the insertion, so the reading frame is restored: the codons from UUC onwards are the same as in the original. [B1]
Only the codons between the two changes (the second and third) are different, so only two amino acids (Asn and Arg instead of Thr and Gly) are changed. [B1]
Q: [6 marks] ★★★ In an experiment to find the genetic code, scientists made artificial mRNA molecules and found the polypeptides that ribosomes made from them. mRNA made only of the base U (UUUUUU…) gave a polypeptide of only phenylalanine. mRNA made of the repeating pair CU (CUCUCUCU…) gave a polypeptide with the amino acids leucine and serine in strict alternation. (a) State the amino acid that UUU codes for. (b) Using the table of codons above, give the codons that are read in the CUCUCU… mRNA, and which of them codes for leucine. (c) Explain why this result is evidence that the code is made of triplets, and not of groups of two or four bases.
H: Write CUCUCUCU… in groups of three, starting at the first base.
H: What would a code of two bases give for a repeating CU sequence? And a code of four?
A: (a) Phenylalanine. [B1]
(b) The codons are CUC and UCU, repeating (CUC UCU CUC UCU…). [B1]
CUC codes for leucine (and UCU for serine). [B1]
(c) In a repeating two-base sequence, a triplet code gives two different codons in turn (CUC, UCU), so two amino acids alternate, as seen. [B1]
A code of two bases would give only one kind of group (CU), so only one amino acid would be made. [B1]
A code of four bases would also give one repeating group (CUCU), so only one amino acid would be made. [B1]
:::

:::quiz
? Which statement describes a gene?
+ a sequence of DNA nucleotides that codes for a polypeptide
- a sequence of three bases on mRNA that codes for an amino acid
- a sequence of amino acids that forms a polypeptide
- a length of RNA that carries amino acids to the ribosome
> A gene is part of a DNA molecule. A triplet or codon is only three bases, the amino acid sequence is the polypeptide, and tRNA carries amino acids.
? What does it mean when the genetic code is described as degenerate?
+ Most amino acids are coded for by more than one codon.
- Each codon codes for more than one amino acid.
- The code changes when DNA is damaged.
- The code is read in overlapping groups of three.
> Sixty-one codons code for 20 amino acids, so most amino acids have several codons. This is why some substitutions are silent.
? A template strand reads 3′–TAC–5′. What are the mRNA codon and the tRNA anticodon?
+ codon AUG, anticodon UAC
- codon ATG, anticodon TAC
- codon UAC, anticodon AUG
- codon AUG, anticodon AUG
> The codon is complementary to the template (TAC gives AUG, using U for T). The anticodon is complementary to the codon, so it is UAC.
? Which enzyme joins RNA nucleotides to make mRNA?
+ RNA polymerase
- DNA polymerase
- DNA ligase
- amylase
> RNA polymerase builds mRNA using a DNA template. DNA polymerase copies DNA and DNA ligase joins fragments of DNA.
? What is an intron?
+ a non-coding sequence that is removed from the primary transcript
- a coding sequence that is joined to others to form mRNA
- a sequence of three bases that stops translation
- the strand of DNA that is not transcribed
> Introns are removed and exons are joined. A stop codon is three bases on mRNA, and the non-transcribed strand is a DNA strand.
? Which row describes the events at a stop codon?
+ no tRNA has a complementary anticodon, so the polypeptide is released
- a tRNA with the anticodon AUG pairs with the codon and adds methionine
- the ribosome moves backwards along the mRNA
- the mRNA is cut into codons
> The stop codons UAA, UAG and UGA have no matching tRNA anticodon. AUG is the start codon (methionine).
? A substitution changes the codon UAC (tyrosine) to UAG. What is the result?
+ a nonsense mutation, which shortens the polypeptide
- a silent mutation, with no change to the polypeptide
- a missense mutation, with one amino acid changed
- a frameshift, with every later amino acid changed
> UAG is a stop codon, so translation stops at that point. A silent mutation would give a codon for tyrosine, a missense mutation would give a different amino acid, and a substitution does not cause a frameshift.
? One base is inserted in the middle of a gene. What is the most likely effect?
+ every amino acid after the insertion is different, because the reading frame shifts
- one amino acid is changed and the rest are unchanged
- the polypeptide is the same, because the code is degenerate
- the polypeptide is one amino acid longer
> An insertion of one base shifts every later codon (a frameshift). Insertion of three bases would add one amino acid and keep the frame.
? Which mutation is least likely to change the polypeptide?
+ a substitution that gives another codon for the same amino acid
- a deletion of one base near the start of the gene
- an insertion of two bases in the middle of the gene
- a substitution that creates a stop codon
> A silent substitution leaves the amino acid sequence unchanged. Both an insertion of one or two bases and a deletion of one base cause a frameshift, and a stop codon shortens the polypeptide.
? Which statement about the genetic code is correct?
+ It is universal: nearly all organisms use the same codons for the same amino acids.
- Each amino acid has exactly one codon.
- The start codon codes for no amino acid.
- Each base is part of two codons, so the code overlaps.
> The code is universal, degenerate and non-overlapping. The start codon AUG codes for methionine.
:::

:::checklist What you can now do
- [ ] I can state that a polypeptide is coded for by a gene, which is a sequence of nucleotides that forms part of a DNA molecule.
- [ ] I can describe the genetic code: triplets, degenerate, non-overlapping, universal, with a start codon and stop codons.
- [ ] I can describe transcription, including the roles of RNA polymerase, the template (transcribed) strand and the non-transcribed strand.
- [ ] I can explain how a eukaryotic primary transcript is modified by removing introns and joining exons to form mRNA.
- [ ] I can describe translation, including the roles of mRNA, codons, tRNA, anticodons and ribosomes.
- [ ] I can transcribe and translate a short sequence using a code table, and find a codon or an anticodon.
- [ ] I can state what a gene mutation is, and explain how substitution, insertion and deletion each affect the polypeptide.
- [ ] I can recognise silent, missense and nonsense mutations and frameshifts, and explain why a frameshift has a larger effect.
:::

:::recap
- A gene is a sequence of nucleotides, part of a DNA molecule, that codes for a polypeptide.
- The genetic code is a triplet code that is degenerate, non-overlapping and universal. AUG is the start codon (methionine); UAA, UAG and UGA are stop codons. 64 codons: 61 code for amino acids.
- Transcription: RNA polymerase uses the template (transcribed) strand to make mRNA by complementary base pairing (U with A), forming phosphodiester bonds 5′ to 3′. The non-transcribed strand is not copied.
- In eukaryotes the primary transcript has its introns (non-coding) removed and its exons (coding) joined to make mRNA, which leaves through a nuclear pore.
- Translation: mRNA binds a ribosome; tRNA with a complementary anticodon pairs with each codon and brings its amino acid; peptide bonds form; the ribosome moves one codon at a time; a stop codon ends translation.
- Codon on mRNA, anticodon on tRNA. Chain: DNA template triplet → mRNA codon → anticodon → amino acid.
- Gene mutation: a change in the sequence of base pairs in DNA that may alter the polypeptide. Substitution, insertion and deletion.
- Substitution: silent (same amino acid, degenerate code), missense (different amino acid) or nonsense (stop codon). Insertion or deletion of 1 or 2 bases: frameshift. A multiple of 3: the frame is kept.
:::

:::links
- read: [CAIE A Level Biology: nucleic acids and protein synthesis notes and questions](https://www.physicsandmathstutor.com/biology-revision/a-level-cie/nucleic-acids-protein-synthesis/) · Physics & Maths Tutor · free revision notes and past-paper questions sorted by topic
- practise: [Nucleic acids and protein synthesis (9700, exams from 2025)](https://www.savemyexams.com/a-level/biology/cie/25/topics/6-nucleic-acids-and-protein-synthesis/) · Save My Exams · notes and exam questions with mark schemes, some free [paid]
- explore: [Learn.Genetics: transcribe and translate a gene](https://learn.genetics.utah.edu/content/basics/transcribe/) · University of Utah · an interactive tool that makes mRNA and a protein from a gene
- explore: [Gene expression essentials](https://phet.colorado.edu/en/simulations/gene-expression-essentials) · PhET · a simulation of transcription and translation, with mutations
- watch: [Amoeba Sisters videos](https://www.youtube.com/@AmoebaSisters/videos) · Amoeba Sisters (YouTube) · a friendly first explanation of protein synthesis and mutations
- read: [Genes and proteins](https://openstax.org/books/biology-2e/pages/15-introduction) · OpenStax Biology 2e · free university textbook chapter on the genetic code, transcription and translation, beyond the syllabus in places

Links checked 24 October 2026.
:::

Next: [Plant tissues and water transport](#bio.planttransport) begins the study of how organisms move substances, starting with plants.
