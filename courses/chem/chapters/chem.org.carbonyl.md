@chapter chem.org.carbonyl
@title Aldehydes and ketones
@level as
@paper CAIE 9701 Papers 1 and 2 (AS); assumed knowledge in Paper 4
@time 5–7 hours
@summary Aldehydes and ketones contain the polar C=O group. You will learn how to make them by oxidising alcohols, how to reduce them back, how HCN adds to the C=O carbon by nucleophilic addition, and how to tell aldehydes from ketones with 2,4-DNPH, Tollens', Fehling's and alkaline iodine.

:::why
Aldehydes and ketones sit in the middle of organic chemistry: alcohols are oxidised to them, and they can be reduced back or built up into longer molecules. The sugar glucose is an aldehyde, the solvent in nail-varnish remover is a ketone, and the chemical tests in this chapter are how a chemist (or an examiner) proves which one is in a bottle. Nucleophilic addition, the mechanism you meet here, also turns up in biochemistry and in the synthesis of many medicines.
:::

**Before you start**, you should know how to name organic compounds from [Introduction to organic chemistry](#chem.org.intro), how alcohols are oxidised from [Alcohols](#chem.org.alcohols), and how curly arrows work from [Halogenoalkanes](#chem.org.halogen).

:::try Warm-up
Q: Propan-1-ol is warmed with acidified potassium dichromate(VI) and the product is distilled off as it forms. Name the product. (from [Alcohols](#chem.org.alcohols))
A: Propanal, an aldehyde. Distilling it out as it forms stops it being oxidised further to propanoic acid.
Q: The Pauling electronegativities are C 2.5 and O 3.5. Which atom of a C=O bond carries the partial positive charge? (from [Chemical bonding](#chem.bonding))
A: Carbon. Oxygen is more electronegative, so it pulls the shared electrons towards itself: \(\ce{C^{\delta+}=O^{\delta-}}\).
Q: In the SN2 mechanism, where does a curly arrow start and where does it end? (from [Halogenoalkanes](#chem.org.halogen))
A: It starts at a lone pair or a bond and ends at the atom (or bond) that receives that pair of electrons. The first arrow starts at a lone pair on the nucleophile and ends at the δ+ carbon.
:::

## The carbonyl group

The C=O group is called the **carbonyl group**. Two families of compound contain it with only carbon and hydrogen attached to the carbonyl carbon.

:::def Aldehyde
A compound with the carbonyl group at the end of a carbon chain, so that the carbonyl carbon is bonded to one hydrogen atom: the functional group is \(\ce{-CHO}\), and the general formula is \(\ce{RCHO}\).
:::

:::def Ketone
A compound with the carbonyl group inside the carbon chain, so that the carbonyl carbon is bonded to two other carbon atoms: the functional group is \(\ce{>C=O}\), and the general formula is \(\ce{RCOR'}\).
:::

R and R′ stand for alkyl groups. Methanal, \(\ce{HCHO}\), has two hydrogens and no alkyl group, and is the one aldehyde where R is hydrogen. An aldehyde and a ketone with the same number of carbon atoms are isomers: propanal \(\ce{CH3CH2CHO}\) and propanone \(\ce{CH3COCH3}\) are both \(\ce{C3H6O}\).

### Shape and polarity

The carbonyl carbon has three bonds (two single, one double) and no lone pair, so the three bonds repel each other as far as possible: they lie in one flat plane at about 120°. This is the **trigonal planar** shape from [Shapes of molecules and ions](#chem.shapes).

Oxygen (3.5) is much more electronegative than carbon (2.5), so the C=O bond is polar, with a δ+ carbon and a δ− oxygen. This one fact explains almost everything in the chapter: the carbon is attacked by species rich in electrons (nucleophiles), and the molecule has a permanent dipole.

:::html
<figure class="fig small"><svg viewBox="0 15 330 120" role="img" aria-label="Displayed formula of ethanal with the C=O carbon at the centre of a flat triangle of three bonds, labelled delta plus on carbon and delta minus on oxygen"><text class="tl tc" x="100" y="89">C</text><text class="tl tc" x="100" y="44">O</text><text class="tl tc" x="62" y="111">CH₃</text><text class="tl tc" x="138" y="111">H</text><path class="ln" d="M97.4 73L97.4 52M102.6 73L102.6 52"/><path class="ln" d="M93 89L75.2 99.4"/><path class="ln" d="M107 89L131 103"/><text class="tl ta" x="116" y="72">δ+</text><text class="tl ta" x="116" y="36">δ−</text><text class="tl" x="190" y="52">trigonal planar</text><text class="tl" x="190" y="69">angles about 120°</text><text class="tl" x="190" y="90">C is δ+: attacked</text><text class="tl" x="190" y="107">by nucleophiles</text></svg><figcaption>Ethanal, CH₃CHO. The carbon of C=O has three bonds in one plane (about 120° apart). Oxygen is more electronegative than carbon, so the C=O bond is polar.</figcaption></figure>
:::

### Naming

:::key Naming aldehydes and ketones
| Family | Ending | Numbering | Examples |
|---|---|---|---|
| aldehyde | -al | the carbon of CHO is always carbon 1, so it needs no number | ethanal \(\ce{CH3CHO}\), butanal \(\ce{CH3CH2CH2CHO}\) |
| ketone | -one | number the chain from the end that gives the C=O carbon the lower number; no number is needed in propanone or butanone | propanone \(\ce{CH3COCH3}\), pentan-2-one \(\ce{CH3COCH2CH2CH3}\), pentan-3-one \(\ce{CH3CH2COCH2CH3}\) |
:::

The final -e of the alkane name is dropped before the ending (butane becomes butanal and butanone). Branches are named as in earlier chapters: \(\ce{(CH3)2CHCHO}\) is 2-methylpropanal.

:::html
<figure class="fig small"><svg viewBox="0 5 345 260" role="img" aria-label="Skeletal formulas of butanal, butanone, pentan-2-one and pentan-3-one"><path class="ln thick" d="M10 70L45 50"/><path class="ln thick" d="M45 50L80 70"/><path class="ln thick" d="M80 70L115 50"/><text class="tl tc" x="115" y="18">O</text><path class="ln thick" d="M112.4 50L112.4 26M117.6 50L117.6 26"/><text class="tl tc" x="145" y="70">H</text><path class="ln thick" d="M115 50L138 62.3"/><text class="tl tc" x="60" y="108">butanal</text><text class="tl tc ta" x="60" y="123">aldehyde</text><path class="ln thick" d="M190 70L225 50"/><path class="ln thick" d="M225 50L260 70"/><path class="ln thick" d="M260 70L295 50"/><text class="tl tc" x="225" y="18">O</text><path class="ln thick" d="M222.4 50L222.4 26M227.6 50L227.6 26"/><text class="tl tc" x="240" y="108">butanone</text><text class="tl tc ta" x="240" y="123">ketone</text><path class="ln thick" d="M10 200L45 180"/><path class="ln thick" d="M45 180L80 200"/><path class="ln thick" d="M80 200L115 180"/><path class="ln thick" d="M115 180L150 200"/><text class="tl tc" x="45" y="148">O</text><path class="ln thick" d="M42.4 180L42.4 156M47.6 180L47.6 156"/><text class="tl tc" x="60" y="238">pentan-2-one</text><text class="tl tc ta" x="60" y="253">ketone</text><path class="ln thick" d="M190 180L225 200"/><path class="ln thick" d="M225 200L260 180"/><path class="ln thick" d="M260 180L295 200"/><path class="ln thick" d="M295 200L330 180"/><text class="tl tc" x="260" y="148">O</text><path class="ln thick" d="M257.4 180L257.4 156M262.6 180L262.6 156"/><text class="tl tc" x="240" y="238">pentan-3-one</text><text class="tl tc ta" x="240" y="253">ketone</text></svg><figcaption>Skeletal formulas. In butanal the C=O carbon is at the end of the chain, so it is carbon 1. In a ketone the C=O carbon is inside the chain; the number in the name says which carbon it is, counting from the end that gives the lower number.</figcaption></figure>
:::

:::eg Name (a) \(\ce{CH3CH2CH2CH2CHO}\), (b) \(\ce{CH3CH2CH2COCH3}\), (c) \(\ce{CH3CH(CH3)CH2CHO}\).
(a) The CHO carbon is carbon 1, and the chain has five carbons: pentanal. [B1]

(b) Six carbons, with the C=O on the second carbon when numbered from the right-hand \(\ce{CH3}\): hexan-2-one. [B1]

(c) The chain through the CHO carbon has four carbons (\(\ce{CHO-CH2-CH-CH3}\)). The methyl branch is on carbon 3: 3-methylbutanal. [B1]
:::

## Physical properties

Aldehydes and ketones have permanent dipoles, so their molecules attract each other by permanent dipole–dipole (pd-pd) forces as well as id-id forces. They cannot form hydrogen bonds with each other, because no hydrogen atom is bonded to oxygen (hydrogen bonding needs an H on N, O or F). That puts their boiling points between those of an alkane and an alcohol of similar relative molecular mass.

| Compound | \(M_r\) | Strongest force between its molecules | Boiling point / °C |
|---|---|---|---|
| propane, \(\ce{CH3CH2CH3}\) | 44.0 | id-id | −42 |
| propanal, \(\ce{CH3CH2CHO}\) | 58.0 | pd-pd (and id-id) | 49 |
| propanone, \(\ce{CH3COCH3}\) | 58.0 | pd-pd (and id-id) | 56 |
| propan-1-ol, \(\ce{CH3CH2CH2OH}\) | 60.0 | hydrogen bonding (and id-id) | 97 |

The small aldehydes and ketones mix with water in all proportions. Water molecules form hydrogen bonds to the carbonyl group: the δ+ hydrogen of water is attracted to a lone pair on the carbonyl oxygen. As the carbon chain grows, the non-polar part gets larger and solubility in water falls. Propanone is a good solvent for both polar and non-polar compounds, which is why it is used in nail-varnish remover.

## Making aldehydes and ketones

Both families are made by oxidising an alcohol with acidified potassium dichromate(VI), \(\ce{K2Cr2O7}\), or acidified potassium manganate(VII), \(\ce{KMnO4}\). The details are in [Alcohols](#chem.org.alcohols); here is the part you need.

| Starting alcohol | Product | Method |
|---|---|---|
| primary | aldehyde | warm with the acidified oxidant and **distil off the aldehyde as it forms** |
| secondary | ketone | warm with the acidified oxidant (distillation or reflux, both work) |

\[\ce{CH3CH2CH2OH + [O] -> CH3CH2CHO + H2O}\]
\[\ce{CH3CH(OH)CH3 + [O] -> CH3COCH3 + H2O}\]

The aldehyde must be distilled out because it is itself easily oxidised to a carboxylic acid. If the mixture were heated under reflux with excess oxidant, the aldehyde would go on to propanoic acid. A ketone has no hydrogen atom on its carbonyl carbon and is not oxidised further by these reagents, so heating a secondary alcohol under reflux is safe. In both cases the colour change of dichromate is orange to green (\(\ce{Cr2O7^2-}\) to \(\ce{Cr^3+}\)). For the distillation apparatus, see the figure in [Alcohols](#chem.org.alcohols); for reflux, see [Halogenoalkanes](#chem.org.halogen).

:::eg Write a balanced ionic equation for the oxidation of propan-2-ol to propanone by acidified manganate(VII), using \(\ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\) and \(\ce{CH3CH(OH)CH3 -> CH3COCH3 + 2H+ + 2e-}\).
The electrons must balance, and the lowest common multiple of 5 and 2 is 10. Multiply the first half-equation by 2 and the second by 5. [M1]
\[\ce{2MnO4- + 16H+ + 5CH3CH(OH)CH3 -> 2Mn^2+ + 8H2O + 5CH3COCH3 + 10H+}\]
Cancel 10 of the 16 \(\ce{H+}\) ions:
\[\ce{2MnO4- + 6H+ + 5CH3CH(OH)CH3 -> 2Mn^2+ + 8H2O + 5CH3COCH3}\] [A1]
The purple solution becomes colourless (very pale pink). [B1]
:::

## Reduction back to alcohols

Reduction is the reverse of oxidation. An aldehyde or ketone is reduced to an alcohol by sodium tetrahydridoborate, \(\ce{NaBH4}\) (in water or ethanol), or by lithium tetrahydridoaluminate, \(\ce{LiAlH4}\) (in dry ether). Both are **reducing agents**: they supply hydrogen, written [H] in equations. \(\ce{NaBH4}\) is the safer, milder one; \(\ce{LiAlH4}\) reacts violently with water, so it must be used in dry ether.

:::key Reduction of aldehydes and ketones
| Starting compound | Product | Example |
|---|---|---|
| aldehyde | primary alcohol | \(\ce{CH3CH2CHO + 2[H] -> CH3CH2CH2OH}\) |
| ketone | secondary alcohol | \(\ce{CH3COCH3 + 2[H] -> CH3CH(OH)CH3}\) |

Reagent: \(\ce{NaBH4}\) or \(\ce{LiAlH4}\) (dry ether). Two hydrogen atoms add across C=O: one to the carbon and one to the oxygen.
:::

The reducing agent works by donating a hydride ion, \(\ce{H-}\), which is a nucleophile that attacks the δ+ carbon. You do not need to draw this mechanism at AS. The reaction links the families: oxidation takes you from alcohol to carbonyl, and reduction takes you back.

:::board
AQA also asks for the mechanism of reduction by NaBH₄: a nucleophilic addition drawn like the HCN mechanism below, with the hydride ion, H⁻, as the nucleophile. Cambridge 9701 asks only for the reagents, the products and the equation with [H].
:::

:::warn NaBH₄ is not an oxidising agent
Examiners often see "NaBH₄ oxidises the ketone". The carbonyl compound gains hydrogen, so it is **reduced**, and NaBH₄ is the **reducing agent**. Dichromate and permanganate are the oxidising agents (they turn alcohols into carbonyl compounds).
:::

:::eg Give the product, with its class, when (a) butanone and (b) butanal are reduced by \(\ce{NaBH4}\).
(a) Butanone, \(\ce{CH3COCH2CH3}\), is a ketone, so it gives a secondary alcohol, butan-2-ol. [B1]
\[\ce{CH3COCH2CH3 + 2[H] -> CH3CH(OH)CH2CH3}\]
(b) Butanal, \(\ce{CH3CH2CH2CHO}\), is an aldehyde, so it gives a primary alcohol, butan-1-ol. [B1]
\[\ce{CH3CH2CH2CHO + 2[H] -> CH3CH2CH2CH2OH}\]
:::

:::eg (Exam style) 2.90 g of butanone is reduced with an excess of \(\ce{NaBH4}\) and 2.05 g of butan-2-ol is collected. Calculate the percentage yield.
The equation is \(\ce{CH3COCH2CH3 + 2[H] -> CH3CH(OH)CH2CH3}\): 1 mol of ketone gives 1 mol of alcohol.

\(M_r(\ce{C4H8O}) = 4(12.0) + 8(1.0) + 16.0 = 72.0\) and \(M_r(\ce{C4H10O}) = 4(12.0) + 10(1.0) + 16.0 = 74.0\). [B1]
\[n(\ce{C4H8O}) = \frac{2.90}{72.0} = 0.04028\,\mathrm{mol}\] [M1]
\[\text{maximum mass of butan-2-ol} = 0.04028 \times 74.0 = 2.981\,\mathrm{g}\] [M1]
\[\text{percentage yield} = \frac{2.05}{2.981} \times 100 = 68.8\,\%\] [A1]
:::

## Nucleophilic addition: HCN

Alkenes, whose \(\ce{C=C}\) is not polar, are attacked by electron-poor species (electrophiles) and undergo **electrophilic addition**. The C=O group is the opposite: its carbon is δ+, so it is attacked by a **nucleophile**, an electron-pair donor. The C=O π bond then breaks, because no atom leaves, and the nucleophile and a hydrogen end up added across the double bond.

:::def Nucleophilic addition
A reaction in which a nucleophile attacks a δ+ carbon of a double bond (such as C=O) and the π bond breaks, so that two groups add across the double bond and nothing is lost from the molecule.
:::

Why does the π bond break and not the whole C=O bond? Using the Data section, C=O is 740 kJ mol⁻¹ and the single bond C–O is 360 kJ mol⁻¹. The π part of the double bond is therefore worth about \(740 - 360 = 380\,\mathrm{kJ\,mol^{-1}}\), and it is the weaker, more exposed part of the bond.

### The reaction

Aldehydes and ketones react with hydrogen cyanide, HCN, to form **hydroxynitriles** (molecules that contain an OH group and a C≡N group). The reagents are HCN with a little KCN as a catalyst, with heat.

\[\ce{CH3CHO + HCN -> CH3CH(OH)CN}\]
\[\ce{CH3COCH3 + HCN -> (CH3)2C(OH)CN}\]

The first product, from ethanal, is 2-hydroxypropanenitrile. The second, from propanone, is 2-hydroxy-2-methylpropanenitrile. A nitrile is named with the carbon of the CN group as carbon 1 (see [Introduction to organic chemistry](#chem.org.intro)), so the OH is on carbon 2 in both. The reaction makes a new C–C bond, so it adds one carbon atom to the chain, like the reaction of a halogenoalkane with KCN.

:::note A safety note about HCN
Hydrogen cyanide is a volatile, extremely poisonous substance. Chemists never handle it directly: the reaction is carried out in a fume cupboard, with a solution of KCN, and acid is added to the mixture so that HCN forms in the flask only as it is used. The cyanide ion itself is also very toxic.
:::

### Why KCN is needed

HCN is a **weak acid**, so most of its molecules stay as HCN and very few split into \(\ce{H+}\) and \(\ce{CN-}\) ions. The attacking species is the cyanide ion, not the HCN molecule (a molecule of HCN has no negative charge and is a poor nucleophile). Adding a little KCN supplies cyanide ions, and the reaction speeds up. The cyanide ion is used and then regenerated, so KCN is a catalyst.

### The mechanism

:::html
<figure class="fig small"><svg viewBox="50 25 310 610" role="img" aria-label="Mechanism of nucleophilic addition of HCN to propanone, in three stages from top to bottom: cyanide ion attacks the delta-plus carbon and the C=O pi bond moves onto oxygen to give an alkoxide ion; the O minus then takes a hydrogen ion from HCN, giving 2-hydroxy-2-methylpropanenitrile and regenerating cyanide ion"><text class="tl tc" x="150" y="99">C</text><text class="tl tc" x="100" y="99">H₃C</text><text class="tl tc" x="200" y="99">CH₃</text><path class="ln" d="M142.5 95L113.8 95"/><path class="ln" d="M157.5 95L186.2 95"/><text class="tl tc" x="150" y="49">O</text><path class="ln" d="M147.4 83L147.4 57M152.6 83L152.6 57"/><text class="tl ta" x="122" y="80">δ+</text><text class="tl ta" x="122" y="50">δ−</text><path class="c1 sw2" d="M153.5 70Q178 66 161 46" marker-end="url(#ahs-red)"/><text class="tl tc" x="150" y="169">CN⁻</text><circle class="fi" cx="141" cy="154" r="1.7"/><circle class="fi" cx="147" cy="154" r="1.7"/><path class="c1 sw2" d="M144.5 149Q127 123 148 109" marker-end="url(#ahs-red)"/><path class="ln" d="M150 190V232" marker-end="url(#ah)"/><text class="tl" x="162" y="215">step 1 (slow)</text><text class="tl tc" x="150" y="344">C</text><text class="tl tc" x="100" y="344">H₃C</text><text class="tl tc" x="200" y="344">CH₃</text><path class="ln" d="M142.5 340L113.8 340"/><path class="ln" d="M157.5 340L186.2 340"/><text class="tl tc" x="150" y="294">O⁻</text><path class="ln" d="M150 329.5L150 300.5"/><text class="tl tc" x="150" y="394">CN</text><path class="ln" d="M150 350.5L150 379.5"/><circle class="fi" cx="146" cy="279" r="1.7"/><circle class="fi" cx="152" cy="279" r="1.7"/><path class="c1 sw2" d="M151 274Q190 246 234 277" marker-end="url(#ahs-red)"/><text class="tl" x="186" y="294">+</text><text class="tl tc" x="235" y="294">H</text><text class="tl tc" x="282" y="294">CN</text><path class="ln" d="M242.5 290L271 290"/><path class="c1 sw2" d="M257 293Q254 318 278 307" marker-end="url(#ahs-red)"/><path class="ln" d="M150 415V457" marker-end="url(#ah)"/><text class="tl" x="162" y="440">step 2 (fast)</text><text class="tl tc" x="150" y="559">C</text><text class="tl tc" x="100" y="559">H₃C</text><text class="tl tc" x="200" y="559">CH₃</text><path class="ln" d="M142.5 555L113.8 555"/><path class="ln" d="M157.5 555L186.2 555"/><text class="tl tc" x="150" y="509">OH</text><path class="ln" d="M150 544.5L150 515.5"/><text class="tl tc" x="150" y="609">CN</text><path class="ln" d="M150 565.5L150 594.5"/><text class="tl" x="225" y="559">+ CN⁻</text></svg><figcaption>Nucleophilic addition of HCN to propanone, read from top to bottom. Step 1: a lone pair on the carbon of CN⁻ forms a bond to the δ+ carbon, and the C=O π bond moves onto oxygen. Step 2: a lone pair on O⁻ takes H⁺ from HCN, and the H–C bond breaks to give CN⁻ again, so CN⁻ is a catalyst.</figcaption></figure>
:::

:::steps
1. The C=O bond is polar, with a δ+ carbon and a δ− oxygen.
2. A lone pair on the carbon atom of \(\ce{CN-}\) forms a new C–C bond to the δ+ carbon (first curly arrow, from the lone pair to the carbon). At the same time the C=O π bond moves onto the oxygen (second curly arrow, from the middle of the C=O bond to the O). The oxygen now carries a negative charge: an intermediate with an \(\ce{O-}\) group. This is the slow step.
3. A lone pair on \(\ce{O-}\) takes the \(\ce{H}\) of an HCN molecule (third curly arrow, from the lone pair to the H), and the H–CN bond breaks, its electrons going onto the CN group (fourth curly arrow, from the bond to the CN).
4. The products are the hydroxynitrile and a fresh \(\ce{CN-}\) ion, which can attack another carbonyl molecule.
:::

:::exam Drawing the mechanism for full marks
Show the dipole on C=O. The first arrow starts at the **lone pair on the carbon** of \(\ce{CN-}\) (not at the negative charge, and not at N) and ends at the δ+ carbon. The second arrow starts in the **middle of the C=O double bond** and ends at O. Draw the intermediate with the \(\ce{O-}\), then arrows from the O⁻ lone pair to the H of HCN and from the H–CN bond to CN, and show \(\ce{CN-}\) regenerated. Many students forget the last step and leave \(\ce{O-}\) as the product.
:::

:::warn Do not mix up the two kinds of addition
Alkenes: **electrophilic** addition, because the electron-rich C=C attacks a δ+ atom (H in HBr). Aldehydes and ketones: **nucleophilic** addition, because a nucleophile attacks the δ+ carbon of C=O. The word in the name tells you what attacks the organic molecule first.
:::

Aldehydes are generally more reactive than ketones in nucleophilic addition. The carbon of an aldehyde has a small hydrogen atom on it, so it is less crowded, and it has only one electron-donating alkyl group (a ketone has two) to reduce its δ+ charge.

:::eg Name the product of the reaction of propanal with HCN, with KCN as catalyst, and say whether the product is chiral.
\[\ce{CH3CH2CHO + HCN -> CH3CH2CH(OH)CN}\] [B1]
The product is 2-hydroxybutanenitrile (four carbons including the carbon of CN, with the OH on carbon 2). [B1]
Carbon 2 is bonded to four different groups: H, OH, CN and \(\ce{CH2CH3}\). It is a chiral centre, so the product has two optical isomers (enantiomers). [B1]
The C=O carbon is trigonal planar, so \(\ce{CN-}\) is equally likely to attack from either face of the plane. The two enantiomers form in equal amounts: a racemic mixture that is not optically active. [B1]
:::

The same reasoning applies to every aldehyde except methanal and to every unsymmetrical ketone. Propanone gives a product with two identical \(\ce{CH3}\) groups, so it has no chiral centre. For the full story of chirality and racemic mixtures, see [Isomerism](#chem.org.isomerism).

## Telling aldehydes and ketones apart

Chemical tests are exam favourites because each one separates a pair of compounds with a clear observation. Four tests work with the carbonyl group, and a fifth idea, ease of oxidation, separates aldehydes from ketones.

### Test 1: 2,4-DNPH (is there a C=O?)

2,4-Dinitrophenylhydrazine, 2,4-DNPH, is dissolved in methanol and acid. Add it to an aldehyde or a ketone and an **orange (or yellow-orange) precipitate** forms. It shows the compound contains C=O in an aldehyde or ketone, and it does not separate the two. Carboxylic acids and esters, which also contain C=O, give no precipitate with this test. The precipitate can be filtered, recrystallised and its melting point measured: comparing that value with a table of melting points identifies the original carbonyl compound.

### Test 2: Tollens' reagent (aldehyde or ketone?)

Tollens' reagent is aqueous silver nitrate made alkaline and then treated with just enough dilute ammonia to dissolve the precipitate, so that it contains the diamminesilver(I) ion, \(\ce{[Ag(NH3)2]+}\). Warm the carbonyl compound with it in a water bath. An **aldehyde** gives a **silver mirror** (or a black precipitate); a ketone gives no change. The silver ions are reduced to silver metal, and the aldehyde is oxidised to a carboxylate ion:

\[\ce{RCHO + 2Ag+ + 3OH- -> RCOO- + 2Ag + 2H2O}\]

:::lab Tollens' reagent
Make Tollens' reagent fresh in a clean test tube, because a dirty tube gives a black deposit instead of a mirror. Add a few drops of dilute sodium hydroxide to aqueous silver nitrate (a brown precipitate forms), then add dilute ammonia drop by drop until the precipitate just dissolves. Add a few drops of the unknown, and warm in a hot water bath (about 60 °C) without shaking. Never store the mixture, because it can form explosive compounds as it stands. Wear eye protection and pour the residue away with plenty of water.
:::

### Test 3: Fehling's solution (aldehyde or ketone?)

Fehling's solution is a deep **blue** solution of copper(II) ions in alkali. Warm it with the compound in a water bath. An **aldehyde** turns it to an **orange-red (brick-red) precipitate** of copper(I) oxide, \(\ce{Cu2O}\); the solution stays blue with a ketone. The copper(II) ions are reduced to copper(I), and the aldehyde is oxidised to a carboxylate:

\[\ce{RCHO + 2Cu^2+ + 5OH- -> RCOO- + Cu2O + 3H2O}\]

Fehling's solution (and the similar Benedict's solution) is also how a laboratory tests for glucose, because glucose in its open-chain form is an aldehyde.

### Test 4: ease of oxidation

An aldehyde has a hydrogen atom on its carbonyl carbon, so it is easily oxidised to a carboxylic acid. Warm it with acidified dichromate(VI) and the orange solution turns **green**; a ketone, with no such hydrogen, does not react under these conditions and the solution stays orange. Acidified manganate(VII) goes from purple to colourless with an aldehyde and does not change with a ketone.

\[\ce{RCHO + [O] -> RCOOH}\]

:::key Distinguishing aldehydes from ketones
| Reagent | Aldehyde | Ketone |
|---|---|---|
| 2,4-DNPH | orange precipitate | orange precipitate |
| Tollens' reagent, warm | silver mirror (or black precipitate) | no change |
| Fehling's solution, warm | blue solution gives an orange-red precipitate | solution stays blue |
| acidified \(\ce{K2Cr2O7}\), warm | orange gives green | stays orange |
:::

:::warn Observations, word for word
A silver mirror forms with an aldehyde only: a ketone does **not** give one. For Fehling's solution, write "blue solution gives an orange-red precipitate", never "blue to red solution" (the product is a solid). For dichromate, write "orange to green". Say what you see, not the name of the product.
:::

:::lab Fehling's solution
Add the carbonyl compound to Fehling's solution in a test tube and warm it in a hot water bath for a few minutes. Look for a change from a clear blue solution to a cloudy orange-red solid. Do not heat the mixture directly with a Bunsen flame, since the contents can spit. Wear eye protection; the solution is alkaline and corrosive.
:::

### Test 5: the iodoform (tri-iodomethane) reaction

Ethanal and the ketones that have a **methyl group next to the C=O**, written \(\ce{CH3CO}{-}\), react with alkaline aqueous iodine (iodine with sodium hydroxide) to give a **pale yellow precipitate of tri-iodomethane**, \(\ce{CHI3}\), together with the carboxylate ion \(\ce{RCOO-}\). The same test detects \(\ce{CH3CH(OH)}{-}\) groups in alcohols, because the alkaline iodine oxidises them to \(\ce{CH3CO}{-}\) first ([Alcohols](#chem.org.alcohols)).

\[\ce{CH3COCH3 + 3I2 + 4OH- -> CHI3 + CH3COO- + 3I- + 3H2O}\]
\[\ce{CH3CHO + 3I2 + 4OH- -> CHI3 + HCOO- + 3I- + 3H2O}\]

| Compound | Has \(\ce{CH3CO}{-}\)? | Yellow precipitate? |
|---|---|---|
| ethanal, \(\ce{CH3CHO}\) | yes (R = H) | yes |
| propanone | yes | yes |
| butanone, pentan-2-one | yes | yes |
| propanal, butanal | no | no |
| pentan-3-one | no (the two groups next to C=O are ethyl groups) | no |

:::tip Reading the group
Look at the two carbon atoms either side of C=O. If one of them is a \(\ce{CH3}\) group, the compound passes the iodoform test. Ethanal passes because its second "group" is the hydrogen of the aldehyde and the other is \(\ce{CH3}\). Propanal does not, because it has \(\ce{CH3CH2}\), not \(\ce{CH3}\), beside the C=O.
:::

:::html
<div class="widget" data-w="chem-orgmap" data-focus="carbonyl"></div>
:::

The reaction map above links alcohols, aldehydes, ketones, carboxylic acids and hydroxynitriles. Follow the arrows from reagent to product.

:::note Spectra
In infrared spectroscopy, the C=O of an aldehyde or ketone absorbs strongly at 1670–1740 cm⁻¹, and in ¹³C NMR (A Level) the carbonyl carbon is at 190–220 ppm. IR is covered in [Infrared spectroscopy and mass spectrometry](#chem.analysis), NMR in [Chromatography and NMR spectroscopy](#chem.analysis2).
:::

:::eg Compound X has the molecular formula \(\ce{C4H8O}\). It gives an orange precipitate with 2,4-DNPH, no change with Tollens' reagent, and a pale yellow precipitate with alkaline aqueous iodine. Identify X.
The orange precipitate with 2,4-DNPH shows that X has a C=O group (an aldehyde or ketone). [B1]
No silver mirror with Tollens' reagent means X is a ketone, not an aldehyde. [B1]
The yellow precipitate shows a \(\ce{CH3CO}{-}\) group. [B1]
The ketone with four carbons is butanone, \(\ce{CH3COCH2CH3}\), which has \(\ce{CH3CO}{-}\). (The other \(\ce{C4H8O}\) carbonyl compounds are aldehydes: butanal and 2-methylpropanal.) [B1]
:::

:::eg (Exam style) Describe how you would distinguish, in the laboratory, between propanal and propanone. State the reagent, the conditions and the observation for each.
Add Tollens' reagent to a sample of each and warm in a water bath. [B1]
Propanal gives a silver mirror (or black precipitate). [B1]
Propanone gives no change. [B1]
(An acceptable alternative: Fehling's solution, warmed. Propanal gives an orange-red precipitate and the blue solution of propanone stays blue.)
:::

:::eg Spot the error: a student distinguishes pentan-3-one from pentanal using Fehling's solution. [3 marks]
The student wrote:

Line 1: Add Fehling's solution to each compound and warm.
Line 2: Pentanal: the blue solution turns red.
Line 3: Pentan-3-one: no change.

Line 1 is correct [B1]. **Line 2 loses the mark: "turns red" suggests a red solution, but the observation is a blue solution giving an orange-red precipitate of copper(I) oxide [B0].** Line 3 is correct (the solution stays blue) [B1].

Correct line 2: the blue solution gives an orange-red (brick-red) precipitate. [B1]

The student scores 2 out of 3. Examiners want the state of the product (a precipitate) because the solid is what you see.
:::

## Putting the chapter together: routes

Carbonyl compounds link several families. From propan-1-ol, for example:

- oxidise (acidified dichromate, distil) to propanal;
- reduce propanal (NaBH₄) to propan-1-ol again;
- add HCN (KCN catalyst, heat) to propanal to make 2-hydroxybutanenitrile, which is one carbon longer;
- oxidise propanal under reflux with excess dichromate to propanoic acid ([Carboxylic acids, esters and nitriles](#chem.org.acids)).

The route-planning skills for several steps come in [Organic synthesis (AS)](#chem.org.synthesis).

:::eg (Real context) A chemist converts ethanol into 2-hydroxypropanenitrile. Give the two steps, with reagents and conditions, and an equation for each.
Step 1: warm ethanol with acidified potassium dichromate(VI) and distil off the ethanal as it forms. [B1]
\[\ce{CH3CH2OH + [O] -> CH3CHO + H2O}\] [B1]
Step 2: react the ethanal with HCN, with KCN as a catalyst, and heat. [B1]
\[\ce{CH3CHO + HCN -> CH3CH(OH)CN}\] [B1]
The product has three carbons, one more than ethanol, because the cyanide ion adds a carbon.
:::

:::try Start easy, finish at exam standard
Q: Name (a) \(\ce{CH3CH2CH2CHO}\), (b) \(\ce{CH3CH2COCH2CH2CH3}\), (c) \(\ce{(CH3)2CHCHO}\).
A: (a) butanal; (b) hexan-3-one (the C=O is carbon 3 from either end of six carbons); (c) 2-methylpropanal.
Q: Give the reagent and conditions to convert propan-2-ol into propanone, and say what colour change you see.
A: Acidified potassium dichromate(VI) (or acidified potassium manganate(VII)), warmed. The orange solution turns green (dichromate). Manganate(VII) goes from purple to colourless.
Q: What is made when pentan-3-one is reduced by \(\ce{NaBH4}\)? What is made from pentanal?
A: Pentan-3-one is a ketone, so it gives a secondary alcohol, pentan-3-ol. Pentanal is an aldehyde, so it gives a primary alcohol, pentan-1-ol.
Q: Name the organic product of butanone with HCN, with KCN as catalyst, and decide whether it is chiral.
A: \(\ce{CH3CH2C(CH3)(OH)CN}\) is 2-hydroxy-2-methylbutanenitrile. Carbon 2 holds four different groups (OH, CN, \(\ce{CH3}\) and \(\ce{CH2CH3}\)), so it is chiral, and a racemic mixture forms because the planar C=O is attacked equally from both faces.
Q: Which of these give a silver mirror with Tollens' reagent: ethanal, propanone, butanal, pentan-2-one?
A: Ethanal and butanal. They are aldehydes. Ketones do not react.
Q: Which of these give a yellow precipitate with alkaline aqueous iodine: ethanal, propanal, butanone, pentan-3-one?
A: Ethanal and butanone, because both contain \(\ce{CH3CO}{-}\). Propanal has \(\ce{CH3CH2}\) beside the C=O, and pentan-3-one has two ethyl groups.
Q: Why is a little KCN added to the mixture of HCN and an aldehyde?
A: HCN is a weak acid and gives very few \(\ce{CN-}\) ions. The nucleophile is \(\ce{CN-}\), so KCN supplies cyanide ions and speeds up step 1.
Q: Write the equation for the reaction of propanal with Fehling's solution, using \(\ce{RCHO}\) with R = \(\ce{CH3CH2}\).
A: \(\ce{CH3CH2CHO + 2Cu^2+ + 5OH- -> CH3CH2COO- + Cu2O + 3H2O}\). The product is a propanoate ion, not the free acid, because the solution is alkaline.
:::

:::try Exam practice ★ to ★★★
Q: [2 marks] ★ Give the reagent and conditions needed to convert butan-2-ol into butanone.
A: Acidified potassium dichromate(VI) (or acidified potassium manganate(VII)) [B1], warm (heat). [B1]
Q: [3 marks] ★ A compound is warmed with Tollens' reagent and a silver mirror forms. State what this shows about the compound, name the type of reaction that happens to it, and write an equation for the reaction of ethanal.
A: The compound is an aldehyde. [B1] It is oxidised. [B1]
\[\ce{CH3CHO + 2Ag+ + 3OH- -> CH3COO- + 2Ag + 2H2O}\] [B1]
Q: [3 marks] ★★ Describe a test that distinguishes pentanal from pentan-3-one, giving the reagent, the conditions and the result for each compound.
H: Choose a reagent that oxidises aldehydes but not ketones.
A: Warm with Fehling's solution (or Tollens' reagent). [B1]
Pentanal: blue solution gives an orange-red precipitate (silver mirror with Tollens'). [B1]
Pentan-3-one: the solution stays blue (no change). [B1]
Q: [6 marks] ★★ Describe the mechanism for the reaction of ethanal with HCN in the presence of KCN. Show the curly arrows, the dipole, the intermediate and the product.
H: There are two steps. The first involves \(\ce{CN-}\) and the second involves HCN.
A: Dipole shown on C=O: \(\ce{C^{\delta+}=O^{\delta-}}\). [B1]
Curly arrow from the lone pair on the carbon of \(\ce{CN-}\) to the δ+ carbon. [B1]
Curly arrow from the C=O π bond to the oxygen. [B1]
Intermediate \(\ce{CH3CH(O-)CN}\) drawn. [B1]
Curly arrow from the lone pair on \(\ce{O-}\) to the H of HCN (with a curly arrow from the H–CN bond to the CN). [B1]
Product \(\ce{CH3CH(OH)CN}\) drawn, with \(\ce{CN-}\) regenerated. [B1]
Q: [4 marks] ★★ (#chem.moles) A 0.725 g sample of propanal is warmed with an excess of Fehling's solution. The equation is \(\ce{RCHO + 2Cu^2+ + 5OH- -> RCOO- + Cu2O + 3H2O}\). Calculate the mass of copper(I) oxide formed.
H: One mole of aldehyde gives one mole of \(\ce{Cu2O}\). \(M_r(\ce{Cu2O}) = 2(63.5) + 16.0\).
A: \(M_r(\ce{C3H6O}) = 3(12.0) + 6(1.0) + 16.0 = 58.0\) and \(M_r(\ce{Cu2O}) = 143.0\). [B1]
\(n(\text{propanal}) = 0.725 / 58.0 = 0.01250\,\mathrm{mol}\) [M1]
\(n(\ce{Cu2O}) = 0.01250\,\mathrm{mol}\) (1 : 1) [M1]
mass \(= 0.01250 \times 143.0 = 1.79\,\mathrm{g}\) [A1]
Q: [4 marks] ★★ (#chem.moles) An excess of Tollens' reagent is warmed with 0.360 g of butanal, \(\ce{CH3CH2CH2CHO}\). Calculate the mass of silver formed. (The equation is \(\ce{RCHO + 2Ag+ + 3OH- -> RCOO- + 2Ag + 2H2O}\).)
H: Each mole of aldehyde gives two moles of silver.
A: \(M_r(\ce{C4H8O}) = 72.0\). [B1]
\(n(\text{butanal}) = 0.360 / 72.0 = 0.00500\,\mathrm{mol}\) [M1]
\(n(\ce{Ag}) = 2 \times 0.00500 = 0.0100\,\mathrm{mol}\) [M1]
mass \(= 0.0100 \times 107.9 = 1.08\,\mathrm{g}\) [A1]
Q: [8 marks] ★★★ Compound X is an unbranched carbonyl compound with the formula \(\ce{C5H10O}\). X gives an orange precipitate with 2,4-DNPH and no silver mirror with Tollens' reagent, but it gives a yellow precipitate with alkaline aqueous iodine. X is reduced by \(\ce{NaBH4}\) to compound Y. When Y is heated with acidified \(\ce{K2Cr2O7}\), it forms X again. (a) Identify X and Y, explaining your reasoning from each observation. (b) State the type of alcohol that Y is. (c) Write the equation for the reduction of X by \(\ce{NaBH4}\), using [H].
H: List the three unbranched isomers of \(\ce{C5H10O}\) that contain C=O before you use the tests.
A: (a) The 2,4-DNPH result shows a C=O group, so X is an aldehyde or ketone. [B1]
No silver mirror shows X is a ketone. [B1]
The yellow precipitate shows a \(\ce{CH3CO}{-}\) group. [B1]
Of the unbranched ketones (pentan-2-one and pentan-3-one) only pentan-2-one has \(\ce{CH3CO}{-}\), so X is pentan-2-one, \(\ce{CH3COCH2CH2CH3}\). [B1]
Y is pentan-2-ol, \(\ce{CH3CH(OH)CH2CH2CH3}\). [B1]
(b) Y is a secondary alcohol (oxidised to a ketone). [B1]
(c) \(\ce{CH3COCH2CH2CH3 + 2[H] -> CH3CH(OH)CH2CH2CH3}\) [B1]
Reasoning: reduction of a ketone gives a secondary alcohol, which dichromate oxidises back to the same ketone. [B1]
Q: [6 marks] ★★★ Propan-1-ol is converted into 2-hydroxybutanenitrile in two steps. (a) Give the reagent and conditions for each step, and the intermediate compound. (b) Explain why the final product is not optically active, even though it contains a chiral centre.
H: Which carbonyl compound does propan-1-ol give when it is distilled with acidified dichromate?
H: What shape is the carbon of a C=O group, and from which sides can \(\ce{CN-}\) approach it?
A: (a) Step 1: acidified potassium dichromate(VI), warm, with the propanal distilled off as it forms. [B1]
The intermediate is propanal, \(\ce{CH3CH2CHO}\). [B1]
Step 2: HCN with a little KCN as catalyst, heat. [B1]
(b) The product \(\ce{CH3CH2CH(OH)CN}\) has a chiral centre at carbon 2. [B1]
The C=O carbon in propanal is trigonal planar, so \(\ce{CN-}\) attacks equally from either face. [B1]
Equal amounts of the two enantiomers form (a racemic mixture), and their effects on plane-polarised light cancel. [B1]
:::

:::try Stretch for A*
Q: [4 marks] ★★★ Butane-2,3-dione, \(\ce{CH3COCOCH3}\), gives the smell of butter. Predict, with a reason, whether it gives (i) an orange precipitate with 2,4-DNPH, (ii) a silver mirror with Tollens' reagent and (iii) a yellow precipitate with alkaline aqueous iodine. Give the structure of the product with an excess of \(\ce{NaBH4}\).
H: Look for a C=O group, a CHO group and a \(\ce{CH3CO}{-}\) group.
H: Each C=O group in the molecule can accept two [H].
A: (i) Yes: it contains C=O (both are ketone groups). [B1]
(ii) No: it has no CHO group, so it is not an aldehyde. [B1]
(iii) Yes: it contains the \(\ce{CH3CO}{-}\) group. [B1]
Excess \(\ce{NaBH4}\) reduces both C=O groups to give butane-2,3-diol, \(\ce{CH3CH(OH)CH(OH)CH3}\). [B1]
Q: [4 marks] ★★★ HCN adds to propanone quickly when a little KCN is present. A student adds a few drops of concentrated sulfuric acid to the mixture and finds that the reaction becomes much slower. Explain this observation.
H: What happens to \(\ce{CN-}\) ions when acid is added?
H: Which species is the nucleophile?
A: The nucleophile is the cyanide ion, \(\ce{CN-}\). [B1]
The acid supplies \(\ce{H+}\), which combines with \(\ce{CN-}\): \(\ce{CN- + H+ -> HCN}\). [B1]
HCN is a weak acid and stays mostly as molecules, so the concentration of \(\ce{CN-}\) falls. [B1]
Fewer nucleophiles means fewer successful attacks on the δ+ carbon in the slow step, so the rate falls. [B1]
:::

:::quiz
? Which of these gives a silver mirror when warmed with Tollens' reagent?
- propanone
- pentan-3-one
+ propanal
- butanone
> Only an aldehyde is oxidised by Tollens' reagent. Propanal has a CHO group. The other three are ketones.
? What is the role of KCN in the reaction between HCN and propanone?
- It is the oxidising agent.
- It is a solvent.
+ It supplies \(\ce{CN-}\) ions, so it is a catalyst.
- It is a reactant that is used up.
> HCN is a weak acid and has very few \(\ce{CN-}\) ions. KCN supplies them. The \(\ce{CN-}\) ion that attacks the carbonyl carbon is regenerated in step 2, so KCN is not used up.
? Propanal is reduced by \(\ce{NaBH4}\). What is formed?
- propan-2-ol
+ propan-1-ol
- propanoic acid
- propanone
> An aldehyde is reduced to a primary alcohol. Propan-2-ol would come from propanone. Propanoic acid is the oxidation product.
? In the mechanism of nucleophilic addition to propanone, where does the first curly arrow start?
- at the negative charge of \(\ce{CN-}\)
+ at the lone pair on the carbon atom of \(\ce{CN-}\)
- at the C=O oxygen
- at the nitrogen atom of \(\ce{CN-}\)
> The arrow shows a pair of electrons moving, so it starts at a lone pair (on carbon) and ends at the δ+ carbon of C=O.
? An excess of Tollens' reagent is warmed with 0.0300 mol of ethanal. What mass of silver forms? (\(A_r\) of Ag = 107.9)
- 3.24 g
+ 6.47 g
- 12.9 g
- 0.0600 g
> \(\ce{RCHO + 2Ag+ + 3OH- -> RCOO- + 2Ag + 2H2O}\): 1 mol of aldehyde gives 2 mol of silver. \(n(\ce{Ag}) = 0.0600\,\mathrm{mol}\), and \(0.0600 \times 107.9 = 6.47\,\mathrm{g}\). The 3.24 g option forgets the factor of 2.
? Which compound gives a yellow precipitate with alkaline aqueous iodine?
- propanal
- pentan-3-one
- butanal
+ pentan-2-one
> The test needs \(\ce{CH3CO}{-}\). Pentan-2-one has a methyl group next to the C=O. Propanal and butanal are aldehydes with CH₂ beside the CHO, and pentan-3-one has ethyl groups on both sides.
? Which statement about Fehling's solution is correct?
- The blue solution turns to a red solution with an aldehyde.
+ The blue solution gives an orange-red precipitate with an aldehyde.
- A ketone gives a silver mirror.
- It is a test for any carbonyl compound.
> Aldehydes reduce the copper(II) ions to copper(I) oxide, which is a solid. Ketones do not react, and 2,4-DNPH (not Fehling's) is the test for any carbonyl compound.
:::

:::checklist What you can now do
- [ ] I can describe how aldehydes (by distillation) and ketones are made by oxidising primary and secondary alcohols with acidified dichromate(VI) or manganate(VII).
- [ ] I can describe the reduction of aldehydes and ketones to primary and secondary alcohols with NaBH₄ or LiAlH₄, using [H] in equations.
- [ ] I can give the reagents and conditions for adding HCN to ethanal and propanone, and name the hydroxynitriles formed.
- [ ] I can draw the mechanism of nucleophilic addition of HCN with curly arrows, the intermediate and the regeneration of CN⁻.
- [ ] I can use 2,4-DNPH to test for a carbonyl group and state the observation.
- [ ] I can distinguish an aldehyde from a ketone with Tollens' reagent, Fehling's solution and acidified dichromate(VI), with the correct observations.
- [ ] I can use alkaline aqueous iodine to detect a CH₃CO– group and name the yellow precipitate.
- [ ] I can name aldehydes and ketones and explain why the C=O bond is polar and planar.
:::

:::recap
- Aldehyde RCHO (C=O at the chain end), ketone RCOR′ (C=O inside the chain). The C=O carbon is trigonal planar, about 120°, and δ+. Boiling points lie between alkanes and alcohols (pd-pd forces, no hydrogen bonding between molecules).
- Made by oxidation: primary alcohol, acidified \(\ce{K2Cr2O7}\) or \(\ce{KMnO4}\), distil gives the aldehyde; secondary alcohol gives the ketone.
- Reduced by NaBH₄ or LiAlH₄ (dry ether): aldehyde to primary alcohol, ketone to secondary alcohol; \(\ce{RCHO + 2[H] -> RCH2OH}\).
- HCN with a KCN catalyst, heat: nucleophilic addition giving a hydroxynitrile (ethanal gives 2-hydroxypropanenitrile, propanone gives 2-hydroxy-2-methylpropanenitrile). The nucleophile is \(\ce{CN-}\), which attacks the δ+ carbon and is regenerated. A new product with four different groups is racemic.
- 2,4-DNPH: orange precipitate with any aldehyde or ketone. Tollens': silver mirror with an aldehyde only. Fehling's: blue solution gives orange-red precipitate with an aldehyde only. Acidified dichromate: orange to green with an aldehyde only.
- Alkaline aqueous iodine: yellow \(\ce{CHI3}\) with ethanal and methyl ketones (\(\ce{CH3CO}{-}\)).
:::

:::links
- read: [Aldehydes and ketones menu](https://www.chemguide.co.uk/organicprops/carbonylmenu.html) · Chemguide · background, preparation, addition of HCN, reduction and the oxidation tests, one page each
- read: [Oxidation of aldehydes and ketones](https://www.chemguide.co.uk/organicprops/carbonyls/oxidation.html) · Chemguide · Tollens' and Fehling's tests, with the equations explained slowly
- read: [Addition to aldehydes and ketones](https://www.chemguide.co.uk/organicprops/carbonyls/addition.html) · Chemguide · the HCN mechanism step by step
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Carboxylic acids, esters and nitriles](#chem.org.acids) oxidises aldehydes one stage further and uses the hydroxynitriles from this chapter.
