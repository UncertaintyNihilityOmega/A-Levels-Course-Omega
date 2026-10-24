# data/plan.py: writes course.json chapters, packages and papers (LEAD plan). Run: py data/plan.py
import json
C = [  # id, title, level, group
 ("bio.overview", "Biology: the course map", "guide", "Start here"),
 ("bio.f.basics", "Biology from zero", "pre", "Start here"),
 ("bio.microscopy", "Microscopy and magnification", "as", "Cells and molecules"),
 ("bio.cells", "Eukaryotic cells and organelles", "as", "Cells and molecules"),
 ("bio.prokaryotes", "Prokaryotes and viruses", "as", "Cells and molecules"),
 ("bio.carbs", "Carbohydrates", "as", "Cells and molecules"),
 ("bio.lipids", "Lipids and water", "as", "Cells and molecules"),
 ("bio.proteins", "Proteins", "as", "Cells and molecules"),
 ("bio.foodtests", "Testing for biological molecules", "as", "Cells and molecules"),
 ("bio.enzymes", "Enzymes", "as", "Cells and molecules"),
 ("bio.enzymes2", "Enzyme kinetics, inhibitors and immobilised enzymes", "as", "Cells and molecules"),
 ("bio.membranes", "Membrane structure and cell signalling", "as", "Cells and molecules"),
 ("bio.movement", "Movement into and out of cells", "as", "Cells and molecules"),
 ("bio.mitosis", "Chromosomes and the mitotic cell cycle", "as", "Genetics at AS"),
 ("bio.dna", "Nucleic acids and DNA replication", "as", "Genetics at AS"),
 ("bio.synthesis", "Protein synthesis and gene mutation", "as", "Genetics at AS"),
 ("bio.planttransport", "Plant tissues and water transport", "as", "Transport and exchange"),
 ("bio.translocation", "Translocation in phloem", "as", "Transport and exchange"),
 ("bio.mammaltransport", "Blood vessels, blood and tissue fluid", "as", "Transport and exchange"),
 ("bio.oxygen", "Transport of oxygen and carbon dioxide", "as", "Transport and exchange"),
 ("bio.heart", "The heart and the cardiac cycle", "as", "Transport and exchange"),
 ("bio.gasexchange", "The gas exchange system", "as", "Transport and exchange"),
 ("bio.disease", "Infectious diseases", "as", "Infection and immunity"),
 ("bio.antibiotics", "Antibiotics and resistance", "as", "Infection and immunity"),
 ("bio.immunity", "The immune response", "as", "Infection and immunity"),
 ("bio.antibodies", "Antibodies and vaccination", "as", "Infection and immunity"),
 ("bio.maths", "Maths skills for biology", "as", "AS skills"),
 ("bio.practical", "Practical skills: investigations (Paper 3)", "as", "AS skills"),
 ("bio.practical2", "Practical skills: microscopy and drawing (Paper 3)", "as", "AS skills"),
 ("bio.energy", "Energy, ATP and respiratory quotient", "a2", "Energy"),
 ("bio.respiration", "Aerobic respiration", "a2", "Energy"),
 ("bio.anaerobic", "Anaerobic respiration and investigating respiration", "a2", "Energy"),
 ("bio.photosynthesis", "Photosynthesis", "a2", "Energy"),
 ("bio.limiting", "Limiting factors in photosynthesis", "a2", "Energy"),
 ("bio.homeostasis", "Homeostasis and the kidney", "a2", "Control and coordination"),
 ("bio.glucose", "Blood glucose, cell signalling and biosensors", "a2", "Control and coordination"),
 ("bio.nerves", "Neurones and action potentials", "a2", "Control and coordination"),
 ("bio.synapses", "Synapses and muscle contraction", "a2", "Control and coordination"),
 ("bio.hormones", "Control and coordination in plants", "a2", "Control and coordination"),
 ("bio.meiosis", "Meiosis and genetic variation", "a2", "Inheritance and evolution"),
 ("bio.inheritance", "Monohybrid inheritance", "a2", "Inheritance and evolution"),
 ("bio.dihybrid", "Dihybrid crosses and the chi-squared test", "a2", "Inheritance and evolution"),
 ("bio.genecontrol", "Genes, phenotype and gene control", "a2", "Inheritance and evolution"),
 ("bio.variation", "Variation and the t-test", "a2", "Inheritance and evolution"),
 ("bio.selection", "Natural and artificial selection", "a2", "Inheritance and evolution"),
 ("bio.evolution", "Evolution and speciation", "a2", "Inheritance and evolution"),
 ("bio.classification", "Classification", "a2", "Ecology and genetic technology"),
 ("bio.biodiversity", "Biodiversity and sampling", "a2", "Ecology and genetic technology"),
 ("bio.conservation", "Conservation", "a2", "Ecology and genetic technology"),
 ("bio.genetech", "Tools of genetic technology", "a2", "Ecology and genetic technology"),
 ("bio.genetech2", "Genetic technology in medicine and agriculture", "a2", "Ecology and genetic technology"),
 ("bio.stats", "Statistics for biologists", "a2", "A Level skills"),
 ("bio.planning", "Planning investigations (Paper 5)", "a2", "A Level skills"),
 ("bio.evaluation", "Analysis, conclusions and evaluation (Paper 5)", "a2", "A Level skills"),
 ("bio.exam.p1", "Paper 1: multiple choice", "guide", "Exam readiness"),
 ("bio.exam.p24", "Papers 2 and 4: structured questions", "guide", "Exam readiness"),
 ("bio.exam.p35", "Papers 3 and 5: the practical skills papers", "guide", "Exam readiness"),
 ("bio.mixed.as", "Mixed practice: AS", "guide", "Exam readiness"),
 ("bio.mixed.a2", "Mixed practice: A Level", "guide", "Exam readiness"),
 ("bio.mock.p1", "Mock Paper 1", "mock", "Exam readiness"),
 ("bio.mock.p2", "Mock Paper 2", "mock", "Exam readiness"),
 ("bio.mock.p3", "Mock Paper 3", "mock", "Exam readiness"),
 ("bio.mock.p4", "Mock Paper 4", "mock", "Exam readiness"),
 ("bio.mock.p5", "Mock Paper 5", "mock", "Exam readiness"),
]
P = [
 ("P1", "Start here", ["bio.overview", "bio.f.basics"], []),
 ("P2", "Cells and microscopes", ["bio.microscopy", "bio.cells", "bio.prokaryotes"], ["bio-magnify"]),
 ("P3", "Biological molecules", ["bio.carbs", "bio.lipids", "bio.proteins"], []),
 ("P4", "Food tests and enzymes", ["bio.foodtests", "bio.enzymes", "bio.enzymes2"], ["bio-enzyme"]),
 ("P5", "Membranes and transport across them", ["bio.membranes", "bio.movement"], ["bio-sav"]),
 ("P6", "Cell cycle, DNA and protein synthesis", ["bio.mitosis", "bio.dna", "bio.synthesis"], ["bio-mitosis", "bio-codon"]),
 ("P7", "Transport in plants", ["bio.planttransport", "bio.translocation"], []),
 ("P8", "Transport in mammals", ["bio.mammaltransport", "bio.oxygen", "bio.heart"], ["bio-odc", "bio-cardiac"]),
 ("P9", "Gas exchange, disease and antibiotics", ["bio.gasexchange", "bio.disease", "bio.antibiotics"], []),
 ("P10", "Immunity", ["bio.immunity", "bio.antibodies"], []),
 ("P11", "Energy and respiration", ["bio.energy", "bio.respiration", "bio.anaerobic"], ["bio-rq"]),
 ("P12", "Photosynthesis", ["bio.photosynthesis", "bio.limiting"], ["bio-limiting"]),
 ("P13", "Homeostasis and plant control", ["bio.homeostasis", "bio.glucose", "bio.hormones"], []),
 ("P14", "Nerves and muscles", ["bio.nerves", "bio.synapses"], ["bio-actionpot", "bio-sarcomere"]),
 ("P15", "Meiosis and genetic crosses", ["bio.meiosis", "bio.inheritance", "bio.dihybrid"], ["bio-punnett", "bio-chisq"]),
 ("P16", "Gene control, variation and selection", ["bio.genecontrol", "bio.variation", "bio.selection"], ["bio-ttest", "bio-hardy"]),
 ("P17", "Evolution, classification and biodiversity", ["bio.evolution", "bio.classification", "bio.biodiversity"], ["bio-diversity"]),
 ("P18", "Conservation and genetic technology", ["bio.conservation", "bio.genetech", "bio.genetech2"], ["bio-gel"]),
 ("P19", "AS skills: maths and Paper 3", ["bio.maths", "bio.practical", "bio.practical2"], []),
 ("P20", "A Level skills: statistics and Paper 5", ["bio.stats", "bio.planning", "bio.evaluation"], []),
 ("P21", "Paper guides", ["bio.exam.p1", "bio.exam.p24", "bio.exam.p35"], []),
 ("P22", "AS mixed practice and AS mocks", ["bio.mixed.as", "bio.mock.p1", "bio.mock.p2"], []),
 ("P23", "A Level mixed practice and Mock Paper 4", ["bio.mixed.a2", "bio.mock.p4"], []),
 ("P24", "Practical mocks", ["bio.mock.p3", "bio.mock.p5"], []),
]
ids = [c[0] for c in C]
AS = ids[ids.index("bio.microscopy"):ids.index("bio.antibodies") + 1]
A2 = ids[ids.index("bio.energy"):ids.index("bio.genetech2") + 1]
papers = [
 {"id": "P1", "title": "Paper 1: Multiple Choice", "chapters": AS + ["bio.maths", "bio.exam.p1", "bio.mixed.as"]},
 {"id": "P2", "title": "Paper 2: AS Level Structured Questions", "chapters": AS + ["bio.maths", "bio.exam.p24", "bio.mixed.as"]},
 {"id": "P3", "title": "Paper 3: Advanced Practical Skills", "chapters": ["bio.microscopy", "bio.foodtests", "bio.enzymes", "bio.movement", "bio.maths", "bio.practical", "bio.practical2", "bio.exam.p35"]},
 {"id": "P4", "title": "Paper 4: A Level Structured Questions", "chapters": A2 + ["bio.stats", "bio.exam.p24", "bio.mixed.a2"]},
 {"id": "P5", "title": "Paper 5: Planning, Analysis and Evaluation", "chapters": ["bio.practical", "bio.stats", "bio.variation", "bio.biodiversity", "bio.planning", "bio.evaluation", "bio.exam.p35"]},
]
seen = [c for p in P for c in p[2]]
assert sorted(seen) == sorted(ids), set(ids) ^ set(seen)
assert len(seen) == len(set(seen))
w = [x for p in P for x in p[3]]
assert len(w) == len(set(w))
for p in papers:
    assert all(c in ids for c in p["chapters"]), p
j = json.load(open('course.json', encoding='utf-8'))
j["chapters"] = [{"id": a, "title": b, "level": c, "group": d} for a, b, c, d in C]
j["aliases"] = {"bio.molecules": "bio.carbs", "bio.control": "bio.nerves", "bio.ecology": "bio.biodiversity"}
j["packages"] = [{"id": a, "title": b, "chapters": c, "widgets": d} for a, b, c, d in P]
j["papers"] = papers
json.dump(j, open('course.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(len(C), 'chapters', len(P), 'packages', len(w), 'widgets;', 'AS', len(AS), 'A2', len(A2))
