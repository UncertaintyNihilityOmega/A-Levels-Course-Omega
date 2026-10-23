@chapter chem.org.isomerism
@title Isomerism
@level as a2
@paper CAIE 9701 Papers 1 and 2 (AS); Paper 4 (A Level section)
@time 5–7 hours
@summary Isomers are compounds with the same molecular formula but different structures. You will learn chain, positional and functional-group isomerism, cis–trans isomerism from restricted rotation about C=C, and optical isomerism from chiral centres, and then (A Level) how enantiomers differ in plane-polarised light and in medicine.

:::why
Two compounds can contain exactly the same atoms and still behave completely differently: one smells of spearmint and its mirror image of caraway, and one form of a drug can heal while its twin does harm. Isomerism explains why the formula alone is never enough in organic chemistry, and it is a standard source of marks in structure questions: "draw all the isomers of C₄H₈", "does this molecule show cis–trans isomerism?", "mark the chiral centre".
:::

:::note Which part is AS and which is A Level
Everything up to "Deducing isomers from a molecular formula" is AS (Papers 1 and 2). The last section, "Optical isomers in medicine and the lab (A Level)", is A Level (Paper 4). AS students can stop before it.
:::

**Before you start**, you should know how to name organic compounds and count σ and π bonds from [Introduction to organic chemistry](#chem.org.intro).

:::try Warm-up
Q: Name \(\ce{CH3CH(CH3)CH2CH3}\). (from [Introduction to organic chemistry](#chem.org.intro))
A: The longest chain has four carbons, with a methyl branch on carbon 2: 2-methylbutane.
Q: What is the hybridisation of the carbon atoms in a C=C bond, and what is the bond angle around them? (from [Introduction to organic chemistry](#chem.org.intro))
A: sp², with bond angles of 120°.
Q: How many σ bonds and π bonds are there in propene, \(\ce{CH2=CHCH3}\)? (from [Introduction to organic chemistry](#chem.org.intro))
A: Propene has 9 atoms and no ring, so 8 σ bonds; the C=C contains 1 π bond.
:::

## Isomers: same formula, different structure

:::def Isomers
Compounds with the same molecular formula but different structural formulas or different arrangements of atoms in space.
:::

There are two big families, and each splits into types. Learn this map first; the rest of the chapter fills it in.

| Family | What differs | Types |
|---|---|---|
| **Structural isomers** | the order in which atoms are bonded (a different structural formula) | chain, positional, functional group |
| **Stereoisomers** | only the arrangement of the same bonds in space (the same structural formula) | geometrical (cis–trans), optical |

:::def Structural isomers
Compounds with the same molecular formula but different structural formulas: the atoms are joined together in a different order.
:::

:::def Stereoisomers
Compounds with the same structural formula but a different arrangement of the atoms in space.
:::

## Structural isomerism

### Chain isomers

**Chain isomers** have different arrangements of the carbon skeleton (straight chain or branched) but the same functional group. Butane and 2-methylpropane are both \(\ce{C4H10}\).

:::html
<figure class="fig small"><svg viewBox="0 0 300 105" role="img" aria-label="Skeletal formulas of butane, a four-carbon chain, and 2-methylpropane, a three-carbon chain with a methyl branch; both are C4H10"><path class="ln thick" d="M30 60L65 40"/><path class="ln thick" d="M65 40L100 60"/><path class="ln thick" d="M100 60L135 40"/><path class="ln thick" d="M200 60L235 40"/><path class="ln thick" d="M235 40L270 60"/><path class="ln thick" d="M235 40L235 6"/><text class="tl tc" x="82" y="95">butane</text><text class="tl tc" x="235" y="95">2-methylpropane</text></svg><figcaption>Two chain isomers of C₄H₁₀. Both have four carbon atoms, but one has a branch.</figcaption></figure>
:::

Chain isomers have similar chemical properties (they have the same functional group) but different physical properties: the branched isomer is usually a more compact molecule with weaker intermolecular forces between molecules, so it has the lower boiling point.

### Positional isomers

**Positional isomers** have the same carbon skeleton and the same functional group, but the group is attached at a different position. Examples are propan-1-ol and propan-2-ol (\(\ce{C3H8O}\)), 1-chloropropane and 2-chloropropane (\(\ce{C3H7Cl}\)), butan-1-ol and butan-2-ol (\(\ce{C4H9OH}\)), and but-1-ene and but-2-ene (\(\ce{C4H8}\), the C=C is at a different position).

Positional isomers differ in the number of carbon atoms joined to the carbon that carries the group. Propan-1-ol is a primary alcohol and propan-2-ol is a secondary alcohol, so they react differently (see [Alcohols](#chem.org.alcohols)).

### Functional-group isomers

**Functional-group isomers** have the same molecular formula but different functional groups. Their chemical properties are quite different.

| Molecular formula | Isomer 1 | Isomer 2 |
|---|---|---|
| \(\ce{C3H6O}\) | propanal, an aldehyde | propanone, a ketone |
| \(\ce{C2H6O}\) | ethanol, an alcohol | methoxymethane, an ether |
| \(\ce{C3H6O2}\) | propanoic acid, a carboxylic acid | methyl ethanoate, an ester |
| \(\ce{C3H6}\) | propene, an alkene | cyclopropane, a cycloalkane |

Ethers (R–O–R′, such as \(\ce{CH3OCH3}\)) are not studied further at AS, but you must be able to give one as the isomer of an alcohol. Aldehydes and ketones with the same number of carbons, and carboxylic acids and esters with the same number of carbons, are always isomers, because they share the general formulas \(\ce{C_nH_{2n}O}\) and \(\ce{C_nH_{2n}O2}\) (see [Introduction to organic chemistry](#chem.org.intro)).

:::warn Isomers have different structures, not different drawings
Turning a molecule round, or bending its chain, does not make a new isomer: \(\ce{CH3CH2CH2CH3}\) drawn as a straight line and drawn as a zigzag is one compound. To decide whether two drawings show the same molecule, **name them**. If the names are the same, the molecules are the same.
:::

### Finding all the structural isomers

When a question asks you to "draw all the isomers", work systematically so that you neither miss one nor draw the same molecule twice.

:::steps
1. Count the hydrogen atoms (counting each halogen atom as a hydrogen atom). If the formula fits \(\ce{C_nH_{2n+2}}\), the molecule is saturated and acyclic: no C=C and no ring.
2. For carbon skeletons, start with the **longest chain** and write it down. Then shorten the chain by one carbon and place that carbon as a **branch** on every possible position, then shorten again.
3. Do not put a branch on an end carbon (that only lengthens the chain) and remember that positions that are mirror images along the chain are the same molecule (2-methylbutane, not 3-methylbutane).
4. Put the functional group on each distinct carbon of each skeleton. Count only distinct positions: check by naming each one.
5. Check that the number you found is sensible, and that every drawing has four bonds to each carbon.
:::

:::eg Draw and name all the structural isomers of \(\ce{C5H12}\).
Five carbons and 12 hydrogens: \(2(5) + 2 = 12\), so it is a saturated alkane with no ring.

Longest chain of 5: \(\ce{CH3CH2CH2CH2CH3}\), **pentane**.

Longest chain of 4, with one methyl branch. The branch cannot go on carbon 1 (that would make a chain of 5). On carbon 2 it gives \(\ce{CH3CH(CH3)CH2CH3}\), **2-methylbutane**. On carbon 3 it gives exactly the same molecule, numbered from the other end. So there is one isomer.

Longest chain of 3, with two methyl branches (4 + 1 = 5 carbons in all). Both go on carbon 2, the only carbon that can take a branch, giving \(\ce{(CH3)4C}\), **2,2-dimethylpropane**.

There are **three** isomers: pentane, 2-methylbutane and 2,2-dimethylpropane.
:::

:::eg Draw and name all the structural isomers of \(\ce{C3H8O}\).
\(\ce{C3H8O}\) has the formula of a saturated molecule with one oxygen, so it can be an alcohol or an ether (there is no C=O, because there is no unsaturation).

Alcohols: the three-carbon chain with OH on carbon 1, \(\ce{CH3CH2CH2OH}\) (propan-1-ol), or on carbon 2, \(\ce{CH3CH(OH)CH3}\) (propan-2-ol). OH on carbon 3 is the same as carbon 1.

Ether: the oxygen sits between two carbon groups, \(\ce{CH3-O-CH2CH3}\), methoxyethane.

There are **three** isomers. The first two are positional isomers of each other; the ether is a functional-group isomer of both.
:::

## Geometrical (cis–trans) isomerism

Stereoisomers have the same structural formula, so the difference must lie in three-dimensional arrangement. The first kind comes from the C=C double bond.

A single bond is a σ bond, and the two ends of a σ bond can turn about it freely. A double bond is different. The π bond is formed by sideways overlap of two p orbitals, and the orbitals overlap only if they stay parallel. Turning one end of the C=C through 90° would pull the p orbitals apart and break the π bond, which needs a large amount of energy. So at ordinary temperatures **there is no rotation about a double bond**, and the groups on the two carbons are locked in position.

:::def Geometrical (cis–trans) isomerism
A type of stereoisomerism in which the groups bonded to the two carbons of a C=C double bond are arranged differently in space, because there is restricted rotation about the π bond. The **cis** isomer has two similar groups on the same side of the double bond; the **trans** isomer has them on opposite sides.
:::

Look at but-2-ene, \(\ce{CH3CH=CHCH3}\). Each carbon of the double bond carries an \(\ce{H}\) and a \(\ce{CH3}\). The two methyl groups can be on the same side or on opposite sides, and the molecule cannot flip from one to the other.

:::html
<figure class="fig small"><svg viewBox="0 25 330 130" role="img" aria-label="Skeletal formulas of cis-but-2-ene, with both methyl groups on the same side of the double bond, and trans-but-2-ene, with the methyl groups on opposite sides"><path class="ln thick" d="M70 67.4L110 67.4M70 72.6L110 72.6"/><text class="tl tc" x="52.5" y="104.3">H</text><path class="ln thick" d="M70 70L52.5 39.7"/><path class="ln thick" d="M70 70L58 90.8"/><text class="tl tc" x="127.5" y="104.3">H</text><path class="ln thick" d="M110 70L127.5 39.7"/><path class="ln thick" d="M110 70L122 90.8"/><path class="ln thick" d="M220 67.4L260 67.4M220 72.6L260 72.6"/><text class="tl tc" x="202.5" y="104.3">H</text><path class="ln thick" d="M220 70L202.5 39.7"/><path class="ln thick" d="M220 70L208 90.8"/><text class="tl tc" x="277.5" y="43.7">H</text><path class="ln thick" d="M260 70L277.5 100.3"/><path class="ln thick" d="M260 70L272 49.2"/><text class="tl tc" x="90" y="140">cis-but-2-ene</text><text class="tl tc" x="240" y="140">trans-but-2-ene</text></svg><figcaption>In cis-but-2-ene the two CH₃ groups are on the same side of the C=C; in trans-but-2-ene they are on opposite sides. The H atoms on the double-bond carbons are drawn so you can see the groups.</figcaption></figure>
:::

The two isomers are different compounds with different physical properties, such as melting point and boiling point, because their shapes differ.

:::key When does cis–trans isomerism occur?
Both conditions must be met:
1. There is a C=C double bond, so rotation is restricted.
2. **Each carbon of the C=C is bonded to two different groups.**
If either carbon has two identical groups, swapping them gives the same molecule and there is no isomerism.
:::

:::note E and Z
You may see E/Z labels on cis–trans isomers (Z is "same side", as cis; E is "opposite sides", as trans). Cambridge accepts them but does not require them, and this course uses cis and trans.
:::

:::eg Decide whether (a) but-1-ene, (b) pent-2-ene, (c) 2-methylbut-2-ene show cis–trans isomerism.
(a) But-1-ene is \(\ce{CH2=CHCH2CH3}\). Carbon 1 has two hydrogen atoms, which are identical. **No isomerism.**

(b) Pent-2-ene is \(\ce{CH3CH=CHCH2CH3}\). Carbon 2 carries \(\ce{H}\) and \(\ce{CH3}\), and carbon 3 carries \(\ce{H}\) and \(\ce{CH2CH3}\): two different groups on each. **Cis–trans isomerism occurs**: cis-pent-2-ene and trans-pent-2-ene.

(c) 2-methylbut-2-ene is \(\ce{(CH3)2C=CHCH3}\). Carbon 2 carries two \(\ce{CH3}\) groups, which are identical. **No isomerism.**
:::

### Cis–trans isomerism in rings

A ring also blocks rotation, because turning a carbon in a ring would break the ring. Two groups on different ring carbons can be on the same face of the ring (cis) or on opposite faces (trans), provided each of the two ring carbons has two different groups. Wedge and hashed bonds show which side of the ring each group is on.

:::html
<figure class="fig small"><svg viewBox="0 8 330 150" role="img" aria-label="Skeletal formulas of cis-1,2-dimethylcyclohexane, with both methyl groups drawn on wedge bonds, and trans-1,2-dimethylcyclohexane, with one wedge and one hashed bond"><path class="ln thick" d="M80 54L111.2 72"/><path class="ln thick" d="M111.2 72L111.2 108"/><path class="ln thick" d="M111.2 108L80 126"/><path class="ln thick" d="M80 126L48.8 108"/><path class="ln thick" d="M48.8 108L48.8 72"/><path class="ln thick" d="M48.8 72L80 54"/><path class="fi" d="M80 54L84 24L76 24Z"/><path class="fi" d="M111.2 72L139.2 60.5L135.2 53.5Z"/><path class="ln thick" d="M250 54L281.2 72"/><path class="ln thick" d="M281.2 72L281.2 108"/><path class="ln thick" d="M281.2 108L250 126"/><path class="ln thick" d="M250 126L218.8 108"/><path class="ln thick" d="M218.8 108L218.8 72"/><path class="ln thick" d="M218.8 72L250 54"/><path class="fi" d="M250 54L254 24L246 24Z"/><path class="ln" d="M285.8 70.1L285.2 68.9M290.5 68.2L289.2 65.8M295.2 66.2L293.2 62.8M299.8 64.3L297.2 59.7M304.5 62.4L301.2 56.6M309.2 60.5L305.2 53.5"/><text class="tl tc" x="80" y="148">cis</text><text class="tl tc" x="250" y="148">trans</text></svg><figcaption>A wedge bond points towards you and a hashed bond points away. In the cis isomer both methyl groups are on the same face of the ring; in the trans isomer they are on opposite faces. The ring stops them swapping places.</figcaption></figure>
:::

:::eg Does (a) 1,3-dimethylcyclohexane or (b) 1,1-dimethylcyclohexane show cis–trans isomerism?
(a) In 1,3-dimethylcyclohexane, ring carbons 1 and 3 each carry one \(\ce{H}\) and one \(\ce{CH3}\): two different groups on each. The two methyl groups can be on the same face (cis) or on opposite faces (trans). **Cis–trans isomerism occurs.**

(b) In 1,1-dimethylcyclohexane both methyl groups are on the same ring carbon, and no ring carbon holds two different groups that could swap sides. **No isomerism.**
:::

## Optical isomerism

The second kind of stereoisomerism does not involve a double bond. It happens in molecules that can exist as two **mirror images that cannot be placed on top of each other**, like your left and right hands.

:::def Chiral centre
A carbon atom bonded to four different atoms or groups. A molecule with one chiral centre exists as two optical isomers.
:::

:::def Optical isomers (enantiomers)
Stereoisomers that are non-superimposable mirror images of each other. They exist because a chiral centre has four different groups arranged tetrahedrally, so the two arrangements cannot be made to match.
:::

:::analogy
Your hands are mirror images, yet you cannot put a right-hand glove on your left hand: turning it round never makes the thumbs line up. A molecule with a chiral centre is like a hand, and the two enantiomers are the "left" and "right" forms. A carbon with two identical groups is like a hockey stick or a mug: its mirror image is the same object, so there is only one form.
:::

Take butan-2-ol, \(\ce{CH3CH(OH)CH2CH3}\). Carbon 2 has four different groups: \(\ce{H}\), \(\ce{OH}\), \(\ce{CH3}\) and \(\ce{CH2CH3}\). Draw the groups so that two bonds are in the plane of the page, one is a wedge (towards you) and one is hashed (away from you). The mirror image has the same four groups, but with the wedge and hash positions swapped to the other side. No rotation can turn one drawing into the other.

:::html
<figure class="fig small"><svg viewBox="0 0 330 160" role="img" aria-label="The two enantiomers of butan-2-ol drawn as mirror images across a dashed mirror line, each with a chiral carbon bonded to CH3, C2H5, OH and H, using a wedge and a hashed bond"><text class="tl tc" x="80" y="82">C*</text><text class="tl tc" x="56" y="52">CH₃</text><text class="tl tc" x="104" y="52">C₂H₅</text><text class="tl tc" x="114" y="106">OH</text><text class="tl tc" x="46" y="106">H</text><path class="ln thick" d="M72.3 68.4L63.7 57.6"/><path class="ln thick" d="M87.7 68.4L96.3 57.6"/><path class="fi" d="M90.3 85.2L101.4 98L106 91.5Z"/><path class="ln" d="M66.5 86.7L67.3 87.8M63.3 88.2L64.8 90.3M60.1 89.6L62.4 92.9M56.9 91.1L60 95.4M53.7 92.5L57.5 98M50.5 94L55.1 100.5"/><text class="tl tc" x="250" y="82">C*</text><text class="tl tc" x="274" y="52">CH₃</text><text class="tl tc" x="226" y="52">C₂H₅</text><text class="tl tc" x="216" y="106">OH</text><text class="tl tc" x="284" y="106">H</text><path class="ln thick" d="M257.7 68.4L266.3 57.6"/><path class="ln thick" d="M242.3 68.4L233.7 57.6"/><path class="fi" d="M239.7 85.2L224 91.5L228.6 98Z"/><path class="ln" d="M262.7 87.8L263.5 86.7M265.2 90.3L266.7 88.2M267.6 92.9L269.9 89.6M270 95.4L273.1 91.1M272.5 98L276.3 92.5M274.9 100.5L279.5 94"/><path class="ln-m thin dash" d="M165 24V128"/><text class="tl tc ta" x="165" y="16">mirror</text><text class="tl tc" x="80" y="150">enantiomer 1</text><text class="tl tc" x="250" y="150">enantiomer 2</text></svg><figcaption>The two enantiomers of butan-2-ol. The carbon marked * is the chiral centre. The wedge comes out of the page and the hashed bond goes behind it. The right-hand molecule is the mirror image of the left, and no rotation can make it match.</figcaption></figure>
:::

The tool below holds two models of a molecule that are mirror images of each other. Press the button to try to rotate the right-hand model so that it matches the left. With a chiral centre it never does: two groups match and the other two are swapped. Choose 2-propanol to see a molecule that is not chiral.

:::html
<div class="widget" data-w="chem-chiral" data-mol="butan-2-ol"></div>
:::

:::key Finding a chiral centre
For each carbon atom with four single bonds, write the four groups attached to it. If **all four are different**, it is a chiral centre. Mark it with an asterisk. Check each carbon in turn; ignore carbons with a double bond or two identical groups (such as \(\ce{CH3}\) or \(\ce{CH2}\)).
:::

Two examples that matter in biology are 2-hydroxypropanoic acid (lactic acid), \(\ce{CH3CH(OH)COOH}\), where carbon 2 has \(\ce{H}\), \(\ce{OH}\), \(\ce{CH3}\) and \(\ce{COOH}\), and the amino acid alanine (2-aminopropanoic acid), \(\ce{CH3CH(NH2)COOH}\), where carbon 2 has \(\ce{H}\), \(\ce{NH2}\), \(\ce{CH3}\) and \(\ce{COOH}\). Each has one chiral centre and exists as two enantiomers.

:::eg Identify the chiral centres in threonine, \(\ce{CH3CH(OH)CH(NH2)COOH}\), and state how many stereoisomers it has.
Look at each carbon with four single bonds, in turn.

- \(\ce{CH3}\): three identical hydrogen atoms, **not** chiral.
- \(\ce{CH(OH)}\), carbon 3: bonded to \(\ce{H}\), \(\ce{OH}\), \(\ce{CH3}\) and \(\ce{CH(NH2)COOH}\): four different groups, **chiral**.
- \(\ce{CH(NH2)}\), carbon 2: bonded to \(\ce{H}\), \(\ce{NH2}\), \(\ce{COOH}\) and \(\ce{CH(OH)CH3}\): four different groups, **chiral**.
- \(\ce{COOH}\): has a C=O, so it has no four single bonds: **not** chiral.

Threonine has **two** chiral centres. With \(n\) different chiral centres a molecule has up to \(2^n\) stereoisomers, so this has \(2^2 = 4\).
:::

:::eg How many stereoisomers does pent-3-en-2-ol, \(\ce{CH3CH(OH)CH=CHCH3}\), have?
Carbon 2 is bonded to \(\ce{H}\), \(\ce{OH}\), \(\ce{CH3}\) and \(\ce{CH=CHCH3}\): a **chiral centre**, which gives 2 optical isomers.

The C=C: carbon 3 carries \(\ce{H}\) and \(\ce{CH(OH)CH3}\), and carbon 4 carries \(\ce{H}\) and \(\ce{CH3}\). Each has two different groups, so there is **cis–trans isomerism**, which gives 2 geometrical isomers.

The two kinds are independent, so \(2 \times 2 = 4\) stereoisomers.
:::

### Chiral centres in rings

A ring carbon can be a chiral centre. It has four different groups if the two paths round the ring from it lead to different places. In 2-methylcyclohexanone (a six-membered ring with a C=O on carbon 1 and a methyl group on carbon 2), carbon 2 is bonded to \(\ce{H}\), \(\ce{CH3}\), the \(\ce{C=O}\) carbon (one way round the ring) and the \(\ce{CH2}\) at carbon 3 (the other way round). All four are different, so carbon 2 is chiral. In methylcyclohexane the ring carbon with the methyl group has the same ring path in both directions, so it is not.

:::warn Four traps in optical isomerism
(1) Missing a chiral centre in a ring. (2) Calling a carbon with a double bond a chiral centre. (3) Defining enantiomers as "mirror images" and stopping: they must be **non-superimposable** mirror images. (4) Saying enantiomers have different boiling points: their physical properties (melting point, boiling point, density, solubility) are identical.
:::

## Deducing isomers from a molecular formula

You may be given a molecular formula and asked for all the isomers, including stereoisomers. The hydrogen count tells you what to look for.

:::steps
1. Compare the number of hydrogen atoms with \(2n + 2\) (for \(n\) carbons, counting halogens as hydrogen). The shortfall, divided by 2, is the number of **double bonds or rings**.
2. Decide which functional groups fit the other atoms (oxygen could be an alcohol, an ether, a C=O group, an acid or an ester).
3. For each, draw every carbon skeleton and every position (chain and positional isomers).
4. Then check each structure for **cis–trans** isomerism and for **chiral centres**.
5. Count and name. Check that no two of your structures have the same name.
:::

:::eg Draw all the isomers of \(\ce{C4H8}\) that are alkenes or cycloalkanes, including stereoisomers.
Four carbons need 10 hydrogen atoms to be saturated, so \(\ce{C4H8}\) has 2 fewer hydrogens than that: one C=C **or** one ring.

Alkenes. On the straight chain of four carbons the C=C can be between carbons 1 and 2 (**but-1-ene**) or between carbons 2 and 3 (**but-2-ene**, which shows cis–trans isomerism, so two stereoisomers: cis and trans). On the branched chain of three carbons with one methyl group, the only C=C position is at the end (**2-methylpropene**, \(\ce{(CH3)2C=CH2}\)), which has two hydrogens on carbon 1 so no cis–trans isomers.

Rings. A four-membered ring (**cyclobutane**) or a three-membered ring with a methyl group (**methylcyclopropane**).

The total is \(1 + 2 + 1 + 1 + 1 = 6\) isomers: but-1-ene, cis-but-2-ene, trans-but-2-ene, 2-methylpropene, cyclobutane and methylcyclopropane.
:::

:::eg How many structural isomers has \(\ce{C4H9Br}\)? Which one has a chiral centre?
\(\ce{C4H9Br}\) behaves as \(\ce{C4H10}\), so it is saturated and acyclic. Two carbon skeletons: butane and 2-methylpropane.

On butane, the Br can be on carbon 1 (1-bromobutane) or carbon 2 (2-bromobutane): carbon 3 and carbon 4 repeat these.

On 2-methylpropane, the Br can be on a methyl carbon (1-bromo-2-methylpropane) or on the central carbon (2-bromo-2-methylpropane).

That makes **four** structural isomers, the same four as in [Halogenoalkanes](#chem.org.halogen). Of these, 2-bromobutane, \(\ce{CH3CHBrCH2CH3}\), is the only one with a chiral centre: carbon 2 has \(\ce{H}\), \(\ce{Br}\), \(\ce{CH3}\) and \(\ce{CH2CH3}\).
:::

:::eg (Real context) Butanoic acid, \(\ce{CH3CH2CH2COOH}\), gives rancid butter its smell. Ethyl ethanoate, \(\ce{CH3COOCH2CH3}\), is a solvent in some nail-varnish removers and smells sweet. (a) Show that they are isomers. (b) State the type of isomerism. (c) Give the name of a chain isomer of butanoic acid.
(a) Butanoic acid has 4 carbons, 8 hydrogens and 2 oxygens: \(\ce{C4H8O2}\). Ethyl ethanoate has \(2 + 2 = 4\) carbons, \(3 + 2 + 3 = 8\) hydrogens and 2 oxygens: \(\ce{C4H8O2}\). Both have \(M_r = 4(12.0) + 8(1.0) + 2(16.0) = 88.0\). The molecular formula is the same, but the structural formulas are different, so they are isomers.

(b) One has a carboxylic acid group and the other an ester group: **functional-group isomerism**.

(c) Keep the acid group and branch the chain: \(\ce{(CH3)2CHCOOH}\), **2-methylpropanoic acid**. A formula alone (\(\ce{C4H8O2}\)) cannot tell you which compound you have, and the two smell nothing alike.
:::

:::eg Spot the error: Explain why but-2-ene shows cis–trans isomerism but but-1-ene does not. [3 marks]
A student wrote this answer.

Line 1: The C=C double bond cannot rotate because of the π bond, so the groups on each carbon are fixed in position.
Line 2: Each carbon of the C=C in but-2-ene has two different groups, H and CH₃, so the two CH₃ groups can be on the same side or on opposite sides.
Line 3: But-1-ene has no cis–trans isomers because it has only one methyl group.

Line 1 is correct [B1]. Line 2 is correct [B1]. **Line 3 is wrong: it is not the number of methyl groups that matters. Carbon 1 of but-1-ene has two identical hydrogen atoms, so swapping them gives the same molecule [B0].**

The student scores 2 out of 3. Correct line 3: carbon 1 of but-1-ene is bonded to two identical H atoms, so there is only one arrangement. [B1]
:::

:::try Start easy, finish at exam standard
Q: State the type of structural isomerism in each pair: (a) pentane and 2-methylbutane, (b) butan-1-ol and butan-2-ol, (c) ethanol and methoxymethane.
A: (a) chain isomerism, (b) positional isomerism, (c) functional-group isomerism.
Q: Draw (give the structural formula of) a chain isomer and a positional isomer of 1-bromobutane.
A: Chain isomer: 1-bromo-2-methylpropane, \(\ce{(CH3)2CHCH2Br}\) (the skeleton changes, the Br is on a primary carbon). Positional isomer: 2-bromobutane, \(\ce{CH3CHBrCH2CH3}\) (same skeleton, Br on carbon 2).
Q: Which of these show cis–trans isomerism: (a) propene, (b) but-2-ene, (c) 1,2-dichloroethene \(\ce{ClCH=CHCl}\), (d) 2-methylpropene?
A: (b) and (c). Propene has two H on one carbon; 2-methylpropene has two CH₃ on one carbon. In 1,2-dichloroethene each carbon has H and Cl.
Q: Mark the chiral centre in each, or say there is none: (a) \(\ce{CH3CH2CH(Cl)CH3}\), (b) \(\ce{CH3CH(Cl)CH3}\), (c) \(\ce{CH3CH2CH2OH}\).
A: (a) carbon 2 (H, Cl, CH₃, CH₂CH₃). (b) none: carbon 2 has two CH₃ groups. (c) none: carbon 1 has two H and no carbon has four different groups.
Q: Which type of isomerism is shown by \(\ce{C3H6O}\) as propanal and propanone?
A: Functional-group isomerism (an aldehyde and a ketone).
Q: Explain why a double bond prevents rotation but a single bond does not.
A: A single bond is a σ bond, and its overlap is unchanged by turning. In a double bond the π bond needs the p orbitals parallel; turning one carbon through 90° breaks the overlap, which needs a lot of energy.
Q: How many stereoisomers does \(\ce{CH3CH(OH)CH2CH3}\) have, and what is the relationship between them?
A: Two, because there is one chiral centre (carbon 2). They are enantiomers: non-superimposable mirror images.
Q: State how many chiral centres lactic acid, \(\ce{CH3CH(OH)COOH}\), has, and name the four groups on it.
A: One chiral centre: carbon 2, bonded to H, OH, CH₃ and COOH.
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the type of structural isomerism shown by each pair. (a) butane and 2-methylpropane (b) propan-1-ol and propan-2-ol (c) propanal and propanone
A: (a) chain [B1] (b) positional [B1] (c) functional group [B1]
Q: [4 marks] ★★ Three compounds have the molecular formula \(\ce{C3H6O2}\): a carboxylic acid and two esters. Give the name and structural formula of each, and state the type of isomerism between the acid and the esters.
H: Esters are named alkyl alkanoate. Between them, the two parts together have three carbons.
A: Propanoic acid, \(\ce{CH3CH2COOH}\) [B1]; methyl ethanoate, \(\ce{CH3COOCH3}\) [B1]; ethyl methanoate, \(\ce{HCOOCH2CH3}\) [B1]; functional-group isomerism [B1]
Q: [4 marks] ★★ (a) State the two conditions that must both be met for a compound to show cis–trans isomerism. (b) Decide whether each of these shows cis–trans isomerism, giving a reason: 3-methylpent-2-ene and 2,3-dimethylbut-2-ene.
A: (a) There is a C=C double bond with restricted rotation [B1], and each carbon of the C=C has two different groups [B1].
(b) 3-methylpent-2-ene, \(\ce{CH3CH=C(CH3)CH2CH3}\): yes, carbon 2 has H and CH₃ and carbon 3 has CH₃ and CH₂CH₃, so each has two different groups. [B1]
2,3-dimethylbut-2-ene, \(\ce{(CH3)2C=C(CH3)2}\): no, each carbon has two identical CH₃ groups. [B1]
Q: [4 marks] ★ Identify which of these molecules has a chiral centre, and mark it: (a) 2-chlorobutane (b) 2-chloropropane (c) 3-methylhexane (d) 2-methylbutane
A: (a) yes, carbon 2 (H, Cl, CH₃, CH₂CH₃) [B1] (b) no, carbon 2 has two CH₃ groups [B1] (c) yes, carbon 3 (H, CH₃, CH₂CH₃, CH₂CH₂CH₃) [B1] (d) no, carbon 2 has two CH₃ groups [B1]
Q: [4 marks] ★★ Alanine is 2-aminopropanoic acid, \(\ce{CH3CH(NH2)COOH}\). (a) Identify the chiral centre and the four groups bonded to it. (b) State the relationship between the two optical isomers of alanine, and explain why they are different compounds.
A: (a) Carbon 2 [B1], bonded to H, NH₂, CH₃ and COOH [B1].
(b) They are mirror images of each other (enantiomers) [B1] that are non-superimposable, so one cannot be rotated to match the other. [B1]
Q: [4 marks] ★★ State the number of stereoisomers of 4-methylhex-2-ene, \(\ce{CH3CH=CHCH(CH3)CH2CH3}\), and explain your answer.
H: Count chiral centres and then look for cis–trans isomerism on the C=C.
A: Carbon 4 is bonded to H, CH₃, CH₂CH₃ and CH=CHCH₃, so it is a chiral centre: 2 optical isomers. [B1]
Carbons 2 and 3 of the C=C each carry two different groups, so cis–trans isomerism occurs: 2 geometrical isomers. [B1]
The two kinds are independent, so \(2 \times 2\) [M1] = 4 stereoisomers. [A1]
Q: [6 marks] ★★★ (a) Explain why 1,4-dimethylcyclohexane shows cis–trans isomerism but 1,1-dimethylcyclohexane does not. (b) State how many chiral centres 2-methylcyclohexanone has, and explain how you decided.
H: In a ring, ask whether the two paths round the ring from a carbon lead to different places.
A: (a) The ring prevents rotation about the C–C bonds, so groups cannot swap sides. [B1] In 1,4-dimethylcyclohexane each of carbons 1 and 4 has two different groups (H and CH₃), so the methyl groups can be on the same face (cis) or opposite faces (trans). [B1] In 1,1-dimethylcyclohexane both methyl groups are on the same carbon, which has two identical groups, so there is only one arrangement. [B1]
(b) One chiral centre, carbon 2. [B1] It is bonded to H, CH₃, the carbon of the C=O (one way round the ring) and the CH₂ of carbon 3 (the other way). [B1] These four groups are all different. [B1]
Q: [5 marks] ★★★ Three isomers of molecular formula \(\ce{C4H8O}\) are carbonyl compounds. (a) Give the name and structural formula of each. (b) State the type of isomerism between butanal and 2-methylpropanal, and between butanal and butanone.
H: Two of them are aldehydes (a carbonyl at the end of the chain) and one is a ketone.
A: (a) butanal, \(\ce{CH3CH2CH2CHO}\) [B1]; 2-methylpropanal, \(\ce{(CH3)2CHCHO}\) [B1]; butanone, \(\ce{CH3COCH2CH3}\) [B1]
(b) Butanal and 2-methylpropanal are chain isomers. [B1] Butanal and butanone are functional-group isomers. [B1]
Q: [4 marks] ★★ (A Level) Explain why a racemic mixture of 2-hydroxypropanoic acid does not rotate plane-polarised light, although each enantiomer on its own does.
A: Each enantiomer rotates the plane of polarised light by the same angle [B1] in opposite directions. [B1] A racemic mixture contains equal amounts of the two [B1], so the rotations cancel and there is no net rotation. [B1]
Q: [4 marks] ★★★ (A Level) Ethanal reacts with hydrogen cyanide to give 2-hydroxypropanenitrile, \(\ce{CH3CH(OH)CN}\), which has a chiral centre. The product is optically inactive. Explain why.
H: The carbon of the C=O is planar (trigonal planar). From which sides can \(\ce{CN-}\) attack?
A: The C=O carbon is trigonal planar. [B1] The cyanide ion can attack from either side of the plane with equal probability. [B1] This makes equal amounts of the two enantiomers: a racemic mixture. [B1] The enantiomers rotate plane-polarised light equally in opposite directions, so there is no net rotation. [B1]
:::

:::try Stretch for A*
Q: [5 marks] ★★★ An alkene has the molecular formula \(\ce{C5H10}\). (a) Give the names of all the structural isomers that are alkenes. (b) State which of them shows cis–trans isomerism, and the total number of alkene stereoisomers, including cis and trans forms. (c) Explain why none of them has a chiral centre.
H: Write the three carbon skeletons first (pentane, 2-methylbutane, and 2,2-dimethylpropane) and ask where a C=C can go.
H: 2,2-dimethylpropane cannot contain a C=C: its central carbon already has four bonds to carbon.
A: (a) pent-1-ene, pent-2-ene, 2-methylbut-1-ene, 3-methylbut-1-ene, 2-methylbut-2-ene (five structural isomers) [B1] [B1] (B1 for 3 correct, B1 for all 5)
(b) Pent-2-ene shows cis–trans isomerism. [B1] Counting cis and trans, there are \(5 + 1 = 6\) alkene stereoisomers. [B1]
(c) Every sp³ carbon in these alkenes is bonded to two identical groups (two H atoms or two CH₃ groups), so none is bonded to four different groups. [B1]
Q: [4 marks] ★★★ (A Level) A student measures the rotation of plane-polarised light by a solution of an organic compound and finds it is zero. She concludes that the compound is not chiral. Evaluate her conclusion, and suggest an experiment that would test whether the compound is chiral.
H: Think about what a racemic mixture would give.
A: A zero reading is also what an equal mixture of two enantiomers (a racemic mixture) gives, because their rotations cancel. [B1] So the compound could be achiral or a racemic mixture of a chiral compound: the conclusion is not justified. [B1] A test: react the sample with a single enantiomer of another chiral substance, such as an enzyme or a chiral reagent. [B1] Only one enantiomer of the compound reacts or reacts faster, so the remaining sample would rotate the plane of polarised light if it were a racemic mixture. [B1]
:::

## Optical isomers in medicine and the lab (A Level)

:::note AS students can stop here
This section is A Level (Paper 4). It builds on the optical isomerism you have just met. If you are studying AS only, go to the quiz and checklist below.
:::

### Plane-polarised light and optical activity

Ordinary light vibrates in all directions at right angles to its path. A **polariser** lets through only the light that vibrates in one plane: this is **plane-polarised light**.

:::html
<figure class="fig small"><svg viewBox="0 10 355 105" role="img" aria-label="Polarimeter: a lamp, a polariser, a tube containing the sample, an analyser and a detector; the plane of the polarised light is turned by an angle alpha in the sample tube"><circle class="fa s-acc sw2" cx="20" cy="60" r="9"/><rect class="fm ln" x="68" y="34" width="8" height="52" rx="2"/><rect class="fa ln" x="118" y="40" width="80" height="40" rx="3"/><rect class="fm ln" x="240" y="34" width="8" height="52" rx="2"/><circle class="fm2 ln" cx="312" cy="60" r="9"/><path class="ln-m thin dash" d="M29 60H64"/><path class="ln-m thin dash" d="M80 60H114"/><path class="ln-m thin dash" d="M202 60H236"/><path class="ln-m thin dash" d="M252 60H300"/><path class="c1 sw2" d="M97 60V42" marker-end="url(#ahs-red)"/><path class="c1 sw2" d="M97 60V78" marker-end="url(#ahs-red)"/><path class="c1 sw2" d="M220 60L229 44.4" marker-end="url(#ahs-red)"/><path class="c1 sw2" d="M220 60L211 75.6" marker-end="url(#ahs-red)"/><text class="tl tc" x="20" y="104">lamp</text><text class="tl tc" x="72" y="104">polariser</text><text class="tl tc" x="158" y="104">sample</text><text class="tl tc" x="244" y="104">analyser</text><text class="tl tc" x="312" y="104">detector</text><text class="tl tc ta" x="97" y="24">plane</text><text class="tl tc ta" x="220" y="24">turned by α</text></svg><figcaption>A polarimeter. The polariser lets through light that vibrates in one plane only. An optically active sample turns that plane by an angle α, and the analyser is rotated to find the new plane.</figcaption></figure>
:::

:::def Optically active
A compound is optically active if it rotates the plane of plane-polarised light. One enantiomer rotates the plane **clockwise** by a certain angle; the other rotates it **anticlockwise** by exactly the same angle.
:::

:::def Racemic mixture
A mixture containing equal amounts of the two enantiomers of a compound. It has no net effect on plane-polarised light, because the rotations cancel, so it is optically inactive.
:::

### What is the same and what differs

Apart from the way it turns plane-polarised light, an enantiomer has **identical physical and chemical properties** to its mirror image: the same melting point, boiling point, density, solubility and reactions with ordinary reagents. A reaction in a flask cannot tell them apart, because the reagents have no left or right.

The difference appears when the molecule meets another chiral molecule. Enzymes and receptors in the body are made of chiral amino acids, so they are chiral, and each fits only one enantiomer, like a glove fitting one hand. Two enantiomers can therefore have **different biological activity**. Examples:

- The two enantiomers of carvone: one smells of spearmint and the other of caraway.
- Thalidomide was sold in the 1950s as a sedative. One of its enantiomers acts as a sedative, and the other causes birth defects. Because the two forms convert into each other in the body, giving only the safe enantiomer would not have prevented the harm; the disaster led to much tighter testing of medicines.

### Why products are often racemic

Many reactions in the lab make racemic mixtures. If a reaction goes through a **planar** intermediate or reactant and creates a chiral centre, the attacking species can approach from either face with equal probability, giving equal amounts of both enantiomers. Two examples from other chapters are the SN1 mechanism of a tertiary halogenoalkane, whose carbocation is planar (see [Halogenoalkanes](#chem.org.halogen)), and nucleophilic addition to the planar C=O group of an aldehyde or ketone (see [Aldehydes and ketones](#chem.org.carbonyl)).

:::eg Explain why the product of the reaction between ethanal and hydrogen cyanide is optically inactive. [4 marks]
\(\ce{CH3CHO + HCN -> CH3CH(OH)CN}\). The product, 2-hydroxypropanenitrile, has a chiral centre at carbon 2 (H, OH, CH₃ and CN), so it exists as two enantiomers.

The carbon of the C=O in ethanal is trigonal planar. [B1] The cyanide ion can attack either face of the plane with equal probability. [B1] Equal amounts of the two enantiomers form, a racemic mixture. [B1] Each enantiomer rotates plane-polarised light by the same angle in opposite directions, so the rotations cancel and there is no net rotation. [B1]
:::

### Chirality in drug synthesis

Because enantiomers can behave differently in the body, the pharmaceutical industry cares about which one it makes. There are three ideas to know.

1. **Different biological activity.** Usually only one enantiomer has the desired effect. The other may be inactive, or may cause side effects.
2. **Racemic mixtures need to be separated.** Ordinary lab synthesis gives a racemic mixture. Separating two enantiomers is difficult, because their physical properties are identical, and it is expensive. At most half of the product is the useful isomer, and the other half is wasted.
3. **Chiral catalysts.** A chiral catalyst (such as an enzyme, or a man-made chiral catalyst) makes mainly one enantiomer, because it fits only one form of the transition state. The advantages of making a single enantiomer are smaller doses, fewer side effects and less waste.

:::eg (Real context) A pharmaceutical firm makes a drug of which only one enantiomer is active. The synthesis gives 6.50 g of the racemic product. (a) What is the maximum mass of the active enantiomer in the product? (b) Separation recovers 85 % of the active enantiomer present. What mass is obtained? (c) A chiral catalyst instead gives a product that is 92 % the active enantiomer by mass. What mass of active enantiomer is in 6.50 g of this product? [5 marks]
(a) A racemic mixture is half of each enantiomer: \(6.50 \times 0.50 = 3.25\) g. [B1]

(b) \(3.25 \times 0.85 = 2.76\) g (to 3 s.f.). [M1] [A1]

(c) \(6.50 \times 0.92 = 5.98\) g. [B1] This is more than twice the mass from separation, and with less waste and no separation step. [B1]
:::

:::try A Level practice
Q: (A Level) State two properties that are the same for two enantiomers and one way in which they differ.
A: Any two of melting point, boiling point, density, solubility, reactions with achiral reagents. They differ in the direction in which they rotate plane-polarised light (equal angles, opposite directions), and in their biological activity.
Q: (A Level) A sample of a chiral compound has a measured rotation of zero. Give two possible explanations.
A: The sample is a racemic mixture (equal amounts of the two enantiomers, so rotations cancel), or the compound is not chiral (no chiral centre), so it is not optically active.
Q: (A Level) State two advantages of using a chiral catalyst, rather than separating a racemic mixture, to make a single-enantiomer drug.
A: Any two of: no wasted half of the product, no costly separation, smaller doses needed, fewer side effects, less waste.
:::

:::quiz
? Which of these alkenes shows cis–trans isomerism?
- but-1-ene
- 2-methylbut-2-ene
+ pent-2-ene
- 2-methylpropene
> Cis–trans isomerism needs two different groups on each carbon of the C=C. Pent-2-ene has H and CH₃ on carbon 2 and H and CH₂CH₃ on carbon 3. But-1-ene has two H on carbon 1, and 2-methylbut-2-ene and 2-methylpropene each have two CH₃ on one carbon.
? Which compound has a chiral centre?
- propan-2-ol
- butan-1-ol
+ butan-2-ol
- 2-methylpropan-2-ol
> Only carbon 2 of butan-2-ol is bonded to four different groups (H, OH, CH₃ and CH₂CH₃). In propan-2-ol and 2-methylpropan-2-ol the key carbon has two or three identical CH₃ groups, and in butan-1-ol no carbon has four different groups.
? How many structural isomers has \(\ce{C5H12}\)?
- 2
+ 3
- 4
- 5
> Pentane, 2-methylbutane and 2,2-dimethylpropane. A methyl branch on carbon 3 of a four-carbon chain is the same as one on carbon 2, so it adds no new isomer.
? The compound \(\ce{CH3CH=CHCH(CH3)CH2CH3}\) has one chiral centre and one C=C that can show cis–trans isomerism. How many stereoisomers does it have?
- 2
- 3
+ 4
- 8
> The chiral centre gives 2 optical isomers and the C=C gives 2 geometrical isomers: \(2 \times 2 = 4\).
? Which pair is an example of functional-group isomerism?
- butan-1-ol and butan-2-ol
- butane and 2-methylbutane
+ propanal and propanone
- cis-but-2-ene and trans-but-2-ene
> Propanal (an aldehyde) and propanone (a ketone) are both \(\ce{C3H6O}\) with different functional groups. The butanols are positional isomers; butane and 2-methylbutane are not isomers (different formulas); the but-2-enes are stereoisomers.
? (A Level) A racemic mixture of a chiral drug is dissolved in water. Which statement is correct?
- It rotates plane-polarised light clockwise.
- It rotates plane-polarised light anticlockwise.
+ It has no net effect on plane-polarised light.
- It contains only one enantiomer.
> A racemic mixture contains equal amounts of the two enantiomers, which rotate the plane by equal angles in opposite directions, so their effects cancel.
:::

:::checklist What you can now do
- [ ] I can define isomers, structural isomers and stereoisomers, and describe chain, positional and functional-group isomerism with examples.
- [ ] I can explain why rotation about a C=C is restricted (the π bond) and state the two conditions for cis–trans isomerism.
- [ ] I can identify cis–trans isomerism in alkenes and in rings, and name the isomers cis and trans.
- [ ] I can define chiral centre and enantiomers, and identify chiral centres in a molecule, including ring carbons.
- [ ] I can deduce all the isomers of a molecular formula, including stereoisomers, and count the stereoisomers of a molecule with one chiral centre and one C=C.
- [ ] (A Level) I can state that enantiomers have identical physical and chemical properties except for rotating plane-polarised light and their biological activity.
- [ ] (A Level) I can describe optical activity, equal rotation in opposite directions, and racemic mixtures, and explain why a racemic product forms from a planar intermediate.
- [ ] (A Level) I can describe why chirality matters in drug synthesis: different biological activity, the need to separate racemic mixtures, and chiral catalysts.
:::

:::recap
- Isomers have the same molecular formula. **Structural** isomers differ in bonding order (chain, positional, functional group); **stereoisomers** have the same structural formula but different arrangement in space (geometrical, optical).
- To list isomers: check the hydrogen count for double bonds or rings, write the longest chain, shorten by one carbon and place it as a branch, then put the functional group in each position; name each to avoid repeats. C₅H₁₂ has 3, C₄H₉Br has 4, C₃H₈O has 3.
- Cis–trans isomerism needs a C=C (restricted rotation, because turning breaks the π bond) **and** two different groups on each carbon of the C=C. It also occurs in rings. But-1-ene has none; but-2-ene has cis and trans.
- A chiral centre is a carbon bonded to four different groups. Enantiomers are non-superimposable mirror images. Mark chiral centres with an asterisk; a ring carbon can be one. With one chiral centre and one cis–trans C=C there are 2 × 2 = 4 stereoisomers.
- (A Level) Enantiomers have identical physical and chemical properties, except that they rotate plane-polarised light by equal angles in opposite directions, and they can have different biological activity. A racemic mixture (equal amounts) is optically inactive.
- (A Level) Planar intermediates (SN1 carbocations, C=O in nucleophilic addition) give racemic products. Single-enantiomer drugs avoid wasted half-products and side effects; chiral catalysts make one enantiomer directly.
:::

:::links
- read: [Structural isomerism](https://www.chemguide.co.uk/basicorg/isomerism/structural.html) · Chemguide · chain, position and functional-group isomers with diagrams
- read: [Geometric (cis/trans) isomerism](https://www.chemguide.co.uk/basicorg/isomerism/geometric.html) · Chemguide · why rotation is restricted and what makes cis and trans forms
- read: [Optical isomerism](https://www.chemguide.co.uk/basicorg/isomerism/optical.html) · Chemguide · chiral centres, enantiomers and how they differ in plane-polarised light
- papers: [CAIE A Level Chemistry 9701 revision](https://www.physicsandmathstutor.com/chemistry-revision/a-level-cie/) · Physics & Maths Tutor · past paper questions sorted by topic [unofficial]

Links checked 23 October 2026.
:::

Next: [Hydrocarbons: alkanes and alkenes](#chem.org.hydrocarbons) uses alkene structure and cis–trans isomerism when it covers addition reactions.
