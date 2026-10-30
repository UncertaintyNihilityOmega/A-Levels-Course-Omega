# FACTS: Biology

Verified exam facts. Chapters state paper details only from this file. Sources: the 9700 syllabus for 2025, 2026
and 2027 (version 1, September 2022; "no significant changes which affect teaching"), read 24 Oct 2026 from the web
archive copy of https://www.cambridgeinternational.org/Images/664560-2025-2027-syllabus.pdf (the board's site was
down), and the front pages of the real May/June 2024 papers 9700/12, 22, 32, 42 and 52 (read 24 Oct 2026).

## Exam structure (syllabus pages 10 and 49)
| Paper | Name | Time | Marks | Questions | AS weight | A Level weight |
|---|---|---|---|---|---|---|
| 1 | Multiple Choice | 1 h 15 min | 40 | 40 four-option (A–D) questions, AS content | 31% | 15.5% |
| 2 | AS Level Structured Questions | 1 h 15 min | 60 | structured questions, AS content | 46% | 23% |
| 3 | Advanced Practical Skills | 2 h | 40 | 2 or 3 questions, laboratory practical, AS content and unfamiliar contexts | 23% | 11.5% |
| 4 | A Level Structured Questions | 2 h | 100 | structured questions, A Level content; AS knowledge required | – | 38.5% |
| 5 | Planning, Analysis and Evaluation | 1 h 15 min | 30 | 2 or more questions, written, no laboratory | – | 11.5% |
- AS Level = topics 1–11; A Level = topics 1–19. Routes: AS only (P1, P2, P3 in one series); A Level staged (AS, then
  P4 and P5 later, carrying the AS result forward); A Level in one series (all five). AS grades a–e; A Level A*–E.
- Series: June and November; March in India only. About 180 guided learning hours for AS, 360 for A Level.
- Assessment objectives: AO1 knowledge and understanding 40%, AO2 handling, applying and evaluating information 40%,
  AO3 experimental skills and investigations 20% (of AS and of A Level). Papers 1, 2, 4: AO1 50% + AO2 50%.
  Papers 3 and 5: AO3 100%.
- Papers 3 and 5 contexts may be outside the syllabus content; any unfamiliar information is given in the question.
  Paper 5 may test AS and A Level content.
- Paper 3 skills marks: manipulation, measurement and observation 15–17; presentation of data and observations
  11–13; analysis, conclusions and evaluation 11–13. Half the candidates start on the microscope work, half on the
  investigation. No dissection of animal material. Microscope: ×10 eyepiece, ×10 and ×40 objectives only.
- Paper 5 skills marks: planning 14–16; analysis, conclusions and evaluation 14–16.

## What the papers print and allow (front pages of the June 2024 papers 9700/12, /22, /32, /42, /52)
- **Every paper: "You may use a calculator."** No data booklet, no formula sheet, no periodic table in any paper.
- Paper 1: "There are forty questions on this paper. Answer all questions." Four possible answers A, B, C and D;
  record the choice in soft pencil on the multiple choice answer sheet. "Each correct answer will score one mark."
  (No mark is taken off for a wrong answer.) Rough working on the question paper.
- Papers 2, 3, 4, 5: answer on the question paper; black or dark blue pen, HB pencil for diagrams and graphs;
  "You should show all your working and use appropriate units." Marks for each part in brackets [ ].
- Real question counts in June 2024 (for the mocks): 9700/22 had 6 questions (14 + 12 + 6 + 17 + 5 + 6 = 60);
  9700/32 had 2 questions (21 + 19 = 40; Q2 was microscope and photomicrograph work); 9700/42 had 10 questions
  (8 + 9 + 11 + 11 + 10 + 11 + 9 + 15 + 8 + 8 = 100); 9700/52 had 2 questions (19 + 11 = 30).
- Statistics formulae (syllabus page 65–66): "Candidates are not expected to remember the formulae … When needed,
  candidates will be provided with this information." The formula is printed inside the question that needs it.
  **Degrees of freedom are NOT given**: χ² df = c − 1 (c = number of classes); t-test df = n₁ + n₂ − 2.
  Tables of critical values are provided when needed. Papers 4 and 5 may give partly completed calculations of
  standard deviation, t, Pearson's r and Spearman's rₛ to finish; chi-squared is only on one row or column of data.

## Statistics (A Level only, syllabus pages 64–67)
- Formulae provided when needed: Hardy–Weinberg p + q = 1 and p² + 2pq + q² = 1; Lincoln index N = (n₁ × n₂)/m₂;
  Simpson's index D = 1 − Σ(n/N)²; χ² = Σ (O − E)²/E; s = √(Σ(x − x̄)²/(n − 1)); SE = s/√n; 95% CI = x̄ ± 2 × SE
  (the syllabus's approximation); t = |x̄₁ − x̄₂| / √(s₁²/n₁ + s₂²/n₂); Pearson r = (Σxy − n x̄ ȳ)/((n − 1) sₓ s_y);
  Spearman rₛ = 1 − 6ΣD²/(n³ − n).
- Use of tests: χ² for nominal (frequency) data, observed v expected. t-test: two samples of continuous data, normally
  distributed, similar standard deviations (fewer than 30 values allowed). Pearson: continuous, normal, scatter shows
  possible linear relationship, at least 5 pairs (ideally 10+). Spearman: not normal / ordinal or rankable,
  independent points, increasing or decreasing relationship, more than 5 pairs (ideally 10–30), random selection.
  Correlation coefficients run from −1 through 0 to +1. Correlation is not causation.
- Critical values (computed by data/crit.py, which matches standard tables):
  χ² at p = 0.05, df 1–10: 3.84, 5.99, 7.81, 9.49, 11.07, 12.59, 14.07, 15.51, 16.92, 18.31.
  χ² at p = 0.01, df 1–5: 6.63, 9.21, 11.34, 13.28, 15.09.
  t (two-tailed) at p = 0.05, df 1–30: 12.71, 4.30, 3.18, 2.78, 2.57, 2.45, 2.36, 2.31, 2.26, 2.23, 2.20, 2.18, 2.16,
  2.14, 2.13, 2.12, 2.11, 2.10, 2.09, 2.09, 2.08, 2.07, 2.07, 2.06, 2.06, 2.06, 2.05, 2.05, 2.05, 2.04.
  Pearson r (two-tailed, p = 0.05) for n pairs 5–12: 0.878, 0.811, 0.754, 0.707, 0.666, 0.632, 0.602, 0.576.
  Spearman rₛ (two-tailed, p = 0.05) for n pairs 5–12, exact (data/spearman_crit.py; = Zar's table and the usual
  biology tables): 1.000, 0.886, 0.786, 0.738, 0.700, 0.648, 0.618, 0.587. The syllabus prints no table (checked
  pp 64–67, 30 Oct 2026); some older tables give 0.591 for n = 12: use 0.587. Always give the value in the question,
  as the exam does.
- Significance in 9700: compare the calculated value with the critical value at p = 0.05. χ²: calculated < critical →
  difference not significant, due to chance, accept the null hypothesis. t: calculated > critical → significant
  difference. r or rₛ: |value| > critical → significant correlation.

## Mathematical requirements (syllabus pages 63–64)
- AS and A Level: prefixes G, M, k, m, µ, n; standard form; symbols < > ⩽ ⩾ / ∝ Σ; estimating; calculator for
  squares, roots, reciprocals, lg, means; significant figures (an answer has the same number as, or one more than,
  the least precise data); magnification and actual size; areas of triangles, rectangles, circles; perimeters and
  circumferences; surface areas and volumes of cuboids and cylinders; mean, median, mode, range; ratios; percentages
  and percentage change; percentage error; line graphs, pie charts, bar charts, histograms (which to use when);
  plotting; ruled lines v best-fit lines; rate from the gradient of a straight line and of a tangent to a curve.
- A Level only: genetic ratios as probabilities; sampling principles; chance and probability; Hardy–Weinberg, Lincoln
  index, Simpson's D; normal v non-normal distributions; mean, median, mode, range, standard deviation, standard
  error, 95% CI; error bars from SD, SE or 95% CI; correlation v causation; χ² and t-tests with df and critical-value
  tables; Pearson and Spearman; when each test is valid.
- Paper 5 concentrations: % (w/v) or mol dm⁻³; serial dilution or proportional dilution.
- Command words (syllabus page 50, verbatim, checked 30 Oct 2026): assess = make an informed judgement; calculate =
  work out from given facts, figures or information; comment = give an informed opinion; compare = identify/comment
  on similarities and/or differences; contrast = identify/comment on differences; define = give precise meaning;
  describe = state the points of a topic / give characteristics and main features; determine = establish an answer
  using the information available; discuss = write about issue(s) or topic(s) in depth in a structured way;
  explain = set out purposes or reasons / make the relationships between things evident / provide why and/or how
  and support with relevant evidence; give = produce an answer from a given source or recall/memory; identify =
  name/select/recognise; outline = set out main points; predict = suggest what may happen based on available
  information; sketch = make a simple drawing showing the key features; state = express in clear terms; suggest =
  apply knowledge and understanding to situations where there are a range of valid responses in order to make
  proposals / put forward considerations. Quote these in the paper guides (bio.exam.p24 has the table).

## Syllabus learning outcomes
Numbering is topic.subtopic.outcome (e.g. 1.1.3). AS = topics 1–11; A Level = 12–19. Short form; the full wording
is copied into each package file.

### 1 Cell structure (AS)
- 1.1 Microscope: 1 temporary preparations for the light microscope; 2 draw cells from slides and photomicrographs;
  3 calculate magnification and actual size from drawings, photomicrographs and electron micrographs (SEM and TEM);
  4 eyepiece graticule and stage micrometer, units mm, µm, nm; 5 define resolution and magnification and explain
  the difference, for light and electron microscopy.
- 1.2 Cells: 1 recognise and outline structure and function of: cell surface membrane; nucleus, nuclear envelope,
  nucleolus; RER; SER; Golgi body; mitochondria (small circular DNA); ribosomes (80S cytoplasm, 70S in chloroplasts and
  mitochondria); lysosomes; centrioles and microtubules; cilia; microvilli; chloroplasts (small circular DNA); cell
  wall; plasmodesmata; large permanent vacuole and tonoplast. 2 describe and interpret photomicrographs, electron
  micrographs and drawings of plant and animal cells; 3 compare plant and animal cells; 4 cells use ATP from
  respiration for energy-requiring processes; 5 prokaryote: unicellular, generally 1–5 µm diameter, peptidoglycan
  wall, circular DNA, 70S ribosomes, no double-membrane organelles; 6 compare prokaryote with plant and animal cells;
  7 viruses are non-cellular: nucleic acid core (DNA or RNA), protein capsid, some have a phospholipid envelope.

### 2 Biological molecules (AS)
- 2.1 Tests: 1 Benedict's (reducing sugars), iodine (starch), emulsion (lipids), biuret (proteins); 2 semi-quantitative
  Benedict's (standardise; time to first colour change or colour standards; estimate concentration); 3 non-reducing
  sugars by acid hydrolysis then Benedict's.
- 2.2 Carbohydrates and lipids: 1 draw ring forms of α- and β-glucose; 2 define monomer, polymer, macromolecule,
  monosaccharide, disaccharide, polysaccharide; 3 covalent bonds join monomers into polymers; 4 glucose, fructose,
  maltose reducing, sucrose non-reducing; 5 glycosidic bond by condensation (disaccharides incl. sucrose,
  polysaccharides); 6 hydrolysis of glycosidic bonds (link to non-reducing test); 7 starch (amylose, amylopectin) and
  glycogen structure–function; 8 cellulose structure and how its arrangement suits cell walls; 9 triglycerides are
  non-polar, hydrophobic: fatty acids (saturated, unsaturated), glycerol, ester bonds; 10 triglyceride structure to
  functions; 11 phospholipids: hydrophilic (polar) phosphate head, hydrophobic (non-polar) fatty acid tails.
- 2.3 Proteins: 1 general amino acid structure, formation and breakage of peptide bond; 2 primary, secondary,
  tertiary, quaternary structure; 3 hydrophobic interactions, hydrogen bonds, ionic bonds, covalent incl. disulfide;
  4 globular generally soluble, physiological roles; fibrous generally insoluble, structural; 5 haemoglobin: two α
  chains (α-globin), two β chains (β-globin), haem group; 6 haemoglobin structure to function, importance of iron in
  haem; 7 collagen molecule and arrangement into fibres; 8 collagen structure to function.
- 2.4 Water: 1 hydrogen bonding between water molecules; properties to roles, limited to solvent action, high specific
  heat capacity, latent heat of vaporisation.

### 3 Enzymes (AS)
- 3.1 Mode of action: 1 globular proteins; intracellular and extracellular; 2 active site, enzyme–substrate complex,
  lowering activation energy, specificity, lock-and-key and induced-fit; 3 investigate progress: rate of product
  formation (catalase) and rate of substrate disappearance (amylase); 4 outline use of a colorimeter.
- 3.2 Factors: 1 investigate and explain temperature, pH (buffer solutions), enzyme concentration, substrate
  concentration, inhibitor concentration; 2 Vmax is used to derive the Michaelis–Menten constant Km, used to compare
  affinity of enzymes for substrates; 3 reversible inhibitors, competitive and non-competitive; 4 investigate enzyme
  immobilised in alginate v free in solution; advantages of immobilised enzymes.

### 4 Cell membranes and transport (AS)
- 4.1 Fluid mosaic: 1 model, hydrophobic and hydrophilic interactions forming the bilayer, arrangement of proteins;
  2 arrangement of cholesterol, glycolipids, glycoproteins; 3 roles of phospholipids, cholesterol, glycolipids,
  proteins, glycoproteins: stability, fluidity, permeability, transport (carrier and channel proteins), cell
  signalling (receptors), cell recognition (antigens); 4 cell signalling: secretion of ligands, transport to target
  cells, binding to cell surface receptors.
- 4.2 Movement: 1 simple diffusion, facilitated diffusion, osmosis, active transport, endocytosis, exocytosis;
  2 investigate diffusion and osmosis with plant tissue, Visking tubing, agar; 3 SA:V decreases with size, calculate
  SA and V of simple 3-D shapes; 4 agar blocks to investigate SA:V and diffusion; 5 immerse plant tissue in solutions
  of different water potential to estimate tissue water potential; 6 water movement in terms of water potential;
  effects on plant and animal cells (solute and pressure potential not expected).

### 5 The mitotic cell cycle (AS)
- 5.1: 1 chromosome structure: DNA, histone proteins, sister chromatids, centromere, telomeres; 2 importance of mitosis
  (growth, replacement of damaged or dead cells, repair, asexual reproduction); 3 cell cycle: interphase (G1, S
  replication, G2), mitosis, cytokinesis; 4 telomeres prevent loss of genes from chromosome ends during replication;
  5 stem cells in replacement and repair; 6 uncontrolled division can form a tumour.
- 5.2: 1 behaviour of chromosomes, nuclear envelope, cell surface membrane and spindle in plant and animal cells
  (prophase, metaphase, anaphase, telophase); 2 interpret photomicrographs, diagrams and slides; identify stages.

### 6 Nucleic acids and protein synthesis (AS)
- 6.1: 1 nucleotide structure incl. ATP (no structural formulae); 2 A and G purines (double ring); C, T, U pyrimidines
  (single ring); 3 DNA double helix: complementary base pairing, antiparallel 5′→3′ and 3′→5′ strands, C–G and A–T
  hydrogen bonding differences, phosphodiester bonds; 4 semi-conservative replication in S phase: DNA polymerase and
  DNA ligase only; leading and lagging strands because DNA polymerase adds nucleotides only 5′ to 3′; 5 RNA structure
  using mRNA.
- 6.2: 1 a polypeptide is coded for by a gene, a sequence of nucleotides forming part of a DNA molecule; 2 universal
  genetic code: triplets code for amino acids or are start and stop codons; 3 transcription and translation: RNA
  polymerase, mRNA, codons, tRNA, anticodons, ribosomes; 4 transcribed (template) strand and non-transcribed strand;
  5 eukaryote primary transcript: introns removed, exons joined to form mRNA; 6 a gene mutation is a change in the
  sequence of base pairs that may alter the polypeptide; 7 substitution, deletion, insertion and their effects.

### 7 Transport in plants (AS)
- 7.1: 1 plan diagrams of TS stems, roots, leaves of herbaceous dicots; 2 distribution of xylem and phloem in them;
  3 draw and label xylem vessel elements, sieve tube elements, companion cells (slides, photomicrographs, EMs);
  4 structure to function of these.
- 7.2: 1 mineral ions and organic compounds transported dissolved in water; 2 water from soil to xylem: apoplast
  (lignin, cellulose) and symplast (endodermis, Casparian strip, suberin); 3 transpiration = evaporation from internal
  leaf surfaces then diffusion of water vapour to the atmosphere; 4 hydrogen bonding: cohesion-tension in
  transpiration pull, adhesion to cellulose; 5 annotated drawings of xerophytic leaf TS; 6 assimilates (sucrose,
  amino acids) move from sources to sinks in sieve tubes; 7 companion cells load sieve tubes: proton pumps and
  cotransporter proteins; 8 mass flow down a hydrostatic pressure gradient from source to sink.

### 8 Transport in mammals (AS)
- 8.1: 1 closed double circulation: heart, blood, arteries, arterioles, capillaries, venules, veins; 2 pulmonary
  artery, pulmonary vein, aorta, vena cava; 3 recognise arteries, veins, capillaries; plan diagrams TS and LS; 4
  structure to function of muscular arteries, elastic arteries, veins, capillaries; 5 recognise and draw red blood
  cells, monocytes, neutrophils, lymphocytes; 6 water main component of blood and tissue fluid: solvent action, high
  specific heat capacity; 7 functions and formation of tissue fluid in a capillary network.
- 8.2: 1 red blood cells and O₂ and CO₂: haemoglobin, carbonic anhydrase, haemoglobinic acid, carbaminohaemoglobin;
  2 chloride shift and its importance; 3 plasma in CO₂ transport; 4 oxygen dissociation curve of adult haemoglobin;
  5 its importance at the partial pressures in lungs and respiring tissues; 6 Bohr shift and its importance.
- 8.3: 1 external and internal structure of the heart; 2 wall thickness: atria v ventricles, left v right ventricle;
  3 cardiac cycle: pressure changes in systole and diastole and valves; 4 SAN, AVN, Purkyne tissue (no nervous or
  hormonal control).

### 9 Gas exchange (AS)
- 9.1: 1 lungs, trachea, bronchi, bronchioles, alveoli, capillary network; 2 distribution of cartilage, ciliated
  epithelium, goblet cells, squamous epithelium of alveoli, smooth muscle, capillaries; 3 recognise these in slides
  and micrographs; 4 recognise trachea, bronchi, bronchioles, alveoli; plan diagrams of TS of trachea and bronchus
  walls; 5 ciliated cells, goblet cells, mucous glands keep the system healthy; 6 functions of cartilage, smooth
  muscle, elastic fibres, squamous epithelium; 7 gas exchange between alveolar air and capillary blood.

### 10 Infectious diseases (AS)
- 10.1: 1 caused by pathogens, transmissible; 2 cholera – bacterium Vibrio cholerae; malaria – protoctists Plasmodium
  falciparum, P. malariae, P. ovale, P. vivax; TB – bacteria Mycobacterium tuberculosis and M. bovis; HIV/AIDS – human
  immunodeficiency virus; 3 transmission of each; 4 biological, social and economic factors in prevention and control
  (no malaria life cycle details).
- 10.2: 1 how penicillin acts on bacteria; why antibiotics do not affect viruses; 2 consequences of antibiotic
  resistance and steps to reduce its impact.

### 11 Immunity (AS)
- 11.1: 1 phagocytes (macrophages, neutrophils); 2 antigen; self v non-self; 3 primary immune response: macrophages,
  B-lymphocytes incl. plasma cells, T-lymphocytes (T-helper and T-killer only); 4 memory cells, secondary response,
  long-term immunity.
- 11.2: 1 antibody structure to function; 2 hybridoma method for monoclonal antibodies; 3 monoclonal antibodies in
  diagnosis and treatment; 4 active v passive, natural v artificial immunity; 5 vaccines contain antigens that
  stimulate long-term immunity; 6 vaccination programmes and control of spread.

### 12 Energy and respiration (A Level)
- 12.1: 1 need for energy: active transport, movement, anabolic reactions (DNA replication, protein synthesis);
  2 features of ATP as universal energy currency; 3 ATP made by substrate-linked phosphorylation and chemiosmosis in
  mitochondrial and chloroplast membranes; 4 relative energy values of carbohydrate, lipid, protein; 5 RQ = CO₂
  produced / O₂ taken in (molecules); 6 calculate RQ from equations; 7 simple respirometers for RQ of germinating seeds
  or small invertebrates.
- 12.2: 1 glycolysis (cytoplasm), link reaction and Krebs cycle (matrix), oxidative phosphorylation (inner membrane);
  2 glycolysis: phosphorylation of glucose, fructose 1,6-bisphosphate (6C) splits to two triose phosphate (3C),
  oxidised to pyruvate (3C), ATP and reduced NAD; 3 with oxygen, pyruvate enters mitochondria; 4 link reaction,
  coenzyme A carries acetyl (2C); 5 Krebs: oxaloacetate (4C) + 2C → citrate (6C), back to oxaloacetate in small
  steps; 6 decarboxylation, dehydrogenation, reduction of NAD and FAD; 7 NAD and FAD carry hydrogen to carriers in the
  inner membrane; 8 oxidative phosphorylation: H atoms → protons + energetic electrons; electrons release energy along
  the ETC (no carrier details); energy pumps protons across the inner membrane; protons return by facilitated
  diffusion through ATP synthase (no details); oxygen is the final electron acceptor, forming water; 9 mitochondrial
  structure and function (diagrams, EMs); 10 anaerobic: lactate fermentation (mammals), ethanol fermentation
  (yeast); 11 why aerobic yield is much greater (no detailed ATP count); 12 rice: aerenchyma, ethanol fermentation in
  roots, faster stem growth; 13 redox indicators (DCPIP, methylene blue): temperature and substrate concentration
  on yeast respiration; 14 simple respirometers: temperature and respiration rate.

### 13 Photosynthesis (A Level)
- 13.1: 1 chloroplast structure to function; 2 ATP and reduced NADP from the light-dependent stage are used in the
  light-independent stage (Calvin cycle); 3 thylakoids (membranes and spaces) in grana: light-dependent; stroma:
  light-independent; 4 chlorophyll a, chlorophyll b, carotene, xanthophyll in light absorption; 5 absorption and
  action spectra; 6 chromatography of pigments, Rf values; 7 cyclic and non-cyclic photophosphorylation; 8 cyclic:
  PSI only, photoactivation, ATP; 9 non-cyclic: PSI and PSII, photoactivation, oxygen-evolving complex catalyses
  photolysis of water, ATP and reduced NADP; 10 electrons release energy along ETC, protons pumped across thylakoid
  membrane, return to stroma through ATP synthase; 11 Calvin cycle: rubisco fixes CO₂ with RuBP (5C) → two GP (3C);
  GP reduced to TP using reduced NADP and ATP; RuBP regenerated from TP using ATP; 12 GP → some amino acids; TP →
  carbohydrates, lipids, amino acids.
- 13.2: 1 light intensity, CO₂ concentration, temperature as limiting factors; 2 explain their effects; 3 redox
  indicators (DCPIP, methylene blue) with chloroplast suspension: light intensity and wavelength; 4 whole plants incl.
  aquatic plants: light intensity, CO₂ concentration, temperature.

### 14 Homeostasis (A Level)
- 14.1: 1 meaning and importance of homeostasis; 2 stimuli, receptors, coordination (nervous, endocrine), effectors
  (muscles, glands), negative feedback; 3 urea from deamination of excess amino acids in the liver; 4 kidney: fibrous
  capsule, cortex, medulla, renal pelvis, ureter, branches of renal artery and vein; 5 nephron: glomerulus, Bowman's
  capsule, PCT, loop of Henle, DCT, collecting duct; 6 urine formation limited to ultrafiltration and selective
  reabsorption in the PCT; 7 structure of Bowman's capsule and PCT to function; 8 hypothalamus, posterior pituitary,
  ADH, aquaporins, collecting ducts in osmoregulation; 9 glucagon signalling: receptor conformational change,
  G-protein, adenylyl cyclase, cAMP second messenger, protein kinase A, enzyme cascade, amplification by
  phosphorylation, glycogen breakdown; 10 negative feedback of blood glucose: insulin on muscle and liver cells,
  glucagon on liver cells; 11 test strips and biosensors: glucose oxidase and peroxidase.
- 14.2: 1 stomata balance CO₂ uptake against water loss; 2 daily rhythms; 3 guard cell structure and mechanism;
  4 abscisic acid closes stomata in water stress, calcium ions as second messenger.

### 15 Control and coordination (A Level)
- 15.1: 1 endocrine system: ADH, glucagon, insulin; 2 compare nervous and endocrine systems; 3 sensory and motor
  neurone structure and function; intermediate (relay) neurones connect them; 4 sensory receptor cells; 5 action
  potential in a sensory neurone from a chemoreceptor in a taste bud; 6 resting potential maintained, events of an
  action potential, restoration in the refractory period; 7 saltatory conduction in myelinated neurones;
  8 refractory period and impulse frequency; 9 cholinergic synapse, role of calcium ions; 10 neuromuscular junction,
  T-tubules, sarcoplasmic reticulum in stimulating contraction of striated muscle; 11 sarcomere ultrastructure;
  12 sliding filament model: troponin, tropomyosin, calcium ions, ATP.
- 15.2: 1 Venus fly trap closure; 2 auxin and elongation: proton pumping acidifies cell walls; 3 gibberellin in
  barley germination.

### 16 Inheritance (A Level)
- 16.1: 1 haploid (n), diploid (2n); 2 homologous pairs; 3 need for reduction division; 4 meiosis stages (prophase I to
  telophase II; not sub-divisions of prophase I) with nuclear envelope, membrane and spindle; 5 interpret
  photomicrographs and diagrams; 6 crossing over and random orientation (independent assortment) give genetically
  different gametes; 7 random fertilisation gives genetically different individuals.
- 16.2: 1 gene, locus, allele, dominant, recessive, codominant, linkage, test cross, F1, F2, phenotype, genotype,
  homozygous, heterozygous; 2 genetic diagrams incl. Punnett squares: monohybrid and dihybrid with dominance,
  codominance, multiple alleles, sex linkage; 3 dihybrid with autosomal linkage and epistasis (expected epistasis
  ratios not required); 4 test crosses; 5 chi-squared test (formula provided); 6 genes → proteins → phenotype: TYR,
  tyrosinase, albinism; HBB, haemoglobin, sickle cell anaemia; F8, factor VIII, haemophilia; HTT, huntingtin,
  Huntington's disease; 7 gibberellin and stem elongation: Le (functional enzyme in gibberellin synthesis), le
  (non-functional).
- 16.3: 1 structural v regulatory genes; repressible v inducible enzymes; 2 lac operon (no cAMP); 3 transcription
  factors in eukaryotes increase or decrease transcription; 4 gibberellin causes breakdown of DELLA proteins, which
  inhibit factors that promote transcription.

### 17 Selection and evolution (A Level)
- 17.1: 1 phenotypic variation: genetic, environmental or both; 2 discontinuous and continuous variation; 3 genetic
  basis of each; 4 t-test to compare means of two samples (formula provided).
- 17.2: 1 natural selection: overproduction, competition, struggle for existence, best adapted survive and pass on
  alleles; 2 stabilising, disruptive, directional selection; 3 selection, founder effect, genetic drift incl.
  bottleneck effect on allele frequencies; 4 antibiotic resistance as natural selection; 5 Hardy–Weinberg
  calculations and conditions (equations provided); 6 principles of selective breeding; 7 disease resistance in wheat
  and rice; inbreeding and hybridisation in maize; milk yield in dairy cattle.
- 17.3: 1 evolution: new species from pre-existing species through changes to gene pools; 2 DNA sequence data and
  evolutionary relationships; 3 speciation by geographical separation (allopatric) and ecological or behavioural
  separation (sympatric).

### 18 Classification, biodiversity and conservation (A Level)
- 18.1: 1 species: biological, morphological, ecological species concepts; 2 three domains Archaea, Bacteria, Eukarya;
  3 Archaea and Bacteria are prokaryotes, differing in membrane lipids, ribosomal RNA, cell wall composition;
  4 kingdom, phylum, class, order, family, genus, species; 5 features of Protoctista, Fungi, Plantae, Animalia;
  6 virus classification by nucleic acid (RNA or DNA), single or double stranded.
- 18.2: 1 define ecosystem and niche; 2 biodiversity levels: ecosystems and habitats; number of species and relative
  abundance; genetic variation within species; 3 importance of random sampling; 4 frame quadrats, line transects, belt
  transects, mark-release-recapture with the Lincoln index (formula provided); 5 Spearman's rank and Pearson's
  correlation (formulae provided), biotic and abiotic factors; 6 Simpson's index of diversity D (formula provided),
  significance of values.
- 18.3: 1 extinction through climate change, competition, hunting by humans, degradation and loss of habitats;
  2 reasons to maintain biodiversity; 3 zoos, botanic gardens, conserved areas (national and marine parks), frozen
  zoos, seed banks; 4 IVF, embryo transfer, surrogacy; 5 reasons to control invasive alien species; 6 IUCN and CITES.

### 19 Genetic technology (A Level)
- 19.1: 1 define recombinant DNA; 2 genetic engineering: deliberate manipulation to modify characteristics, may
  transfer a gene so it is expressed; 3 genes extracted from donor DNA, synthesised from mRNA, or synthesised
  chemically; 4 restriction endonucleases, DNA ligase, plasmids, DNA polymerase, reverse transcriptase; 5 why a
  promoter may be transferred too; 6 marker genes coding for fluorescent products; 7 gene editing: insertion,
  deletion or replacement at specific sites; 8 PCR steps, Taq polymerase; 9 gel electrophoresis; 10 microarrays for
  genome analysis and detecting mRNA; 11 benefits of sequence and structure databases.
- 19.2: 1 recombinant human proteins: insulin, factor VIII, adenosine deaminase; 2 genetic screening: BRCA1 and BRCA2,
  Huntington's disease, cystic fibrosis; 3 gene therapy: SCID, inherited eye diseases; 4 social and ethical issues.
- 19.3: 1 GM for food: GM salmon, herbicide-resistant soybean, insect-resistant cotton; 2 ethical and social
  implications of GMOs in food production.

### Practical assessment (Papers 3 and 5): syllabus pages 51–62
Paper 3 skills (full list copied into packages P19): decisions (IV, DV, range, at least five values and intervals,
how to change IV and measure DV, replicates, controls, standardised variables), microscope (set up, find and draw
tissues and cells, temporary stained slide, actual sizes from magnification, scale bars, graticules, estimate counts
by sampling), hazards and risk (low, medium, high), plan diagrams (no cells, correct proportions), cell drawings
(shapes, wall thickness with two lines or three where cells touch, proportions, observable contents only), tables
(headings with units, IV left or above, no units in the body, consistent decimal places), significant figures
(same as or one more than the least in the data), graphs (IV on x, labelled axes with units, scale using most of the
grid and readable to half a square, crosses or dot-in-circle, best-fit line or curve or ruled point-to-point, no
extrapolation unless justified), bar charts and histograms, drawings (sharp pencil, unbroken lines, most of the space,
no shading), interpreting (calculations, read graphs, estimate concentrations from qualitative results, identify
unknowns by food tests, anomalies, patterns and trends, confidence in conclusions), conclusions (hypothesis
supported?, predictions, explanations), errors (systematic v random: systematic may not affect the trend, random may),
improvements (better standardisation, more accurate measuring of the DV, smaller intervals, replicates and means),
extensions. Paper 3 apparatus and materials list: syllabus pages 56–58.
Paper 5 skills: prediction (words or sketch graph) linked to a hypothesis, IV, DV, key standardised variables;
methods (vary IV, measure IV and DV accurately to suitable precision, standardise, volumes and concentrations,
serial or proportional dilution, controls, logical sequence, anomalies, spread using SD, SE or 95% CI, validity:
accuracy and repeatability, risk assessment with severity and probability, precautions); data (tables and graphs,
error bars, choose calculations, means, percentages, rates, percentage gain or loss, use SD or SE to judge
significance, choose and justify statistical tests, null hypothesis, types of data: nominal, ordinal, continuous);
conclusions (main conclusions, key points, extent hypothesis is supported, strengths and weaknesses of evidence,
explanations, further predictions); evaluation (anomalies and explanations, replication, range and intervals of IV,
suitability of the DV measurement, control of variables, validity, confidence, improvements).
