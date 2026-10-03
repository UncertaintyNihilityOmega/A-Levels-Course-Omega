import os
import json
S = []
def subj(id, title, short, code, files, desc):
    s = dict(id=id, title=title, short=short, code=code, files=files, desc=desc, chapters=[]); S.append(s); return s
def ch(s, id, title, level, file, owner, group):
    s['chapters'].append(dict(id=id, title=title, level=level, file=file, owner=owner, group=group))

s = subj('start','Start Here','Start','GUIDE',['home.md','start.md'],'What A Levels are, how they work, and how to choose subjects')
g='Welcome'
ch(s,'home','Home','start','home.md','ME',g)
for i,t,l in [('start.what','What are A Levels?','start'),('start.boards','Exam boards and how the exams work','start'),('start.grades','Grades, marks and UCAS points','start'),('start.choose','Choosing your subjects','start'),('start.howto','How to use this guide','start')]:
    ch(s,i,t,l,'start.md','R1',g)

s = subj('road','Preparation Roadmap','Roadmap','ROAD',['roadmap-1.md','roadmap-2.md'],'A step-by-step road from day one to results day')
g='The road to exam day'
for i,t,l in [('road.overview','The preparation road at a glance','guide'),('road.planner','Build your personal study plan','tool'),('road.foundations','Phase 1: Fix your foundations','guide'),('road.learn','Phase 2: Learn the content','guide'),('road.practice','Phase 3: Practise and test yourself','guide'),('road.pastpapers','Phase 4: Past papers and mark schemes','guide'),('road.final','Phase 5: Final revision','guide'),('road.examday','Phase 6: Exam day, results and resits','guide')]:
    ch(s,i,t,l,'roadmap-1.md','R1',g)
g='Skills that raise grades'
for i,t,l in [('road.methods','Study methods that actually work','guide'),('road.technique','Exam technique','guide'),('road.commands','Command words decoded','ref'),('road.wellbeing','Motivation, sleep and stress','guide'),('road.resources','The best resources by subject','ref')]:
    ch(s,i,t,l,'roadmap-2.md','R2',g)
g='Beyond the exams'
for i,t,l in [('road.private','Studying as a private candidate','guide'),('road.university','University applications and admissions tests','guide')]:
    ch(s,i,t,l,'roadmap-2.md','R2',g)

s = subj('math','Mathematics','Maths','9709',['math-0.md','math-1a.md','math-1.md','math-2.md','math-3.md','math-3b.md','math-4.md'],'Pure, Statistics and Mechanics from counting to calculus')
g='Before you start'
for i,t,l in [('math.overview','Mathematics: the course map','guide'),('math.f.numbers','Numbers, fractions and percentages','pre'),('math.f.algebra','Algebra from scratch','pre'),('math.f.powers','Powers, roots, surds and standard form','pre'),('math.f.graphs','Coordinates and straight lines','pre'),('math.f.geometry','Geometry and basic trigonometry','pre')]:
    ch(s,i,t,l,'math-0.md','M1',g)
g='Pure Mathematics 1'
ch(s,'math.p1.quadratics','Quadratics','as','math-1a.md','ME',g)
for i,t,l in [('math.p1.functions','Functions','as'),('math.p1.coord','Coordinate geometry','as'),('math.p1.circular','Circular measure','as'),('math.p1.trig','Trigonometry','as'),('math.p1.series','Series','as'),('math.p1.diff','Differentiation','as'),('math.p1.integ','Integration','as')]:
    ch(s,i,t,l,'math-1.md','M1',g)
g='Pure Mathematics 2 and 3'
for i,t,l in [('math.p3.algebra','Algebra: modulus, polynomials and partial fractions','as a2'),('math.p3.logs','Logarithms and exponentials','as'),('math.p3.trig','Further trigonometry','as'),('math.p3.diff','Further differentiation','as'),('math.p3.integ','Further integration','a2'),('math.p3.numerical','Numerical solution of equations','as'),('math.p3.vectors','Vectors','a2'),('math.p3.diffeq','Differential equations','a2'),('math.p3.complex','Complex numbers','a2')]:
    ch(s,i,t,l,'math-2.md','M2',g)
g='Probability and Statistics'
for i,t,l in [('math.s1.data','Representing and summarising data','as'),('math.s1.perms','Permutations and combinations','as'),('math.s1.prob','Probability','as'),('math.s1.drv','Discrete random variables: binomial and geometric','as'),('math.s1.normal','The normal distribution','as'),('math.s.regression','Correlation and regression (UK boards)','as')]:
    ch(s,i,t,l,'math-3.md','M3',g)
for i,t,l in [('math.s2.poisson','The Poisson distribution','a2'),('math.s2.linear','Linear combinations of random variables','a2'),('math.s2.crv','Continuous random variables','a2'),('math.s2.sampling','Sampling and estimation','a2'),('math.s2.hypothesis','Hypothesis testing','a2')]:
    ch(s,i,t,l,'math-3b.md','M3b',g)
g='Mechanics'
for i,t,l in [('math.m.forces','Forces and equilibrium','as'),('math.m.kinematics','Kinematics: describing motion','as'),('math.m.newton',"Newton's laws and connected particles",'as'),('math.m.momentum','Momentum and collisions','as'),('math.m.energy','Work, energy and power','as'),('math.m.projectiles','Projectiles and moments (UK boards)','a2')]:
    ch(s,i,t,l,'math-4.md','M4',g)
g='Further Mathematics'
ch(s,'math.further','Further Mathematics: a guided tour','ext','math-4.md','M4',g)

s = subj('phys','Physics','Physics','9702',['phys-1.md','phys-2.md','phys-3.md'],'From measurement to quantum physics and cosmology')
g='Start here'
for i,t,l in [('phys.overview','Physics: the course map','guide'),('phys.f.basics','Physics from zero','pre')]:
    ch(s,i,t,l,'phys-1.md','P1',g)
g='AS Level'
for i,t in [('phys.units','Physical quantities, units and uncertainty'),('phys.kinematics','Kinematics'),('phys.dynamics','Dynamics and momentum'),('phys.forces','Forces, density and pressure'),('phys.energy','Work, energy and power'),('phys.solids','Deformation of solids'),('phys.waves','Waves'),('phys.superposition','Superposition'),('phys.electricity','Electricity'),('phys.dc','D.C. circuits'),('phys.particles','Particle physics')]:
    ch(s,i,t,'as','phys-1.md','P1',g)
g='A Level (A2)'
for i,t in [('phys.circular','Motion in a circle'),('phys.gravity','Gravitational fields'),('phys.temperature','Temperature and thermal physics'),('phys.gases','Ideal gases'),('phys.thermo','Thermodynamics'),('phys.oscillations','Oscillations'),('phys.efields','Electric fields'),('phys.capacitance','Capacitance')]:
    ch(s,i,t,'a2','phys-2.md','P2',g)
for i,t in [('phys.magnetic','Magnetic fields and electromagnetic induction'),('phys.ac','Alternating currents'),('phys.quantum','Quantum physics'),('phys.nuclear','Nuclear physics'),('phys.medical','Medical physics'),('phys.astro','Astronomy and cosmology')]:
    ch(s,i,t,'a2','phys-3.md','P3',g)
g='Practical physics'
ch(s,'phys.practical','Practical skills and data analysis','guide','phys-3.md','P3',g)

s = subj('chem','Chemistry','Chemistry','9701',['chem-1.md','chem-2.md','chem-3.md','chem-4.md'],'Atoms, reactions and the chemistry of carbon')
g='Start here'
for i,t,l in [('chem.overview','Chemistry: the course map','guide'),('chem.f.basics','Chemistry from zero','pre')]:
    ch(s,i,t,l,'chem-1.md','C1',g)
g='Physical chemistry'
for i,t in [('chem.atoms','Atomic structure'),('chem.moles','Moles and stoichiometry'),('chem.bonding','Chemical bonding'),('chem.states','States of matter'),('chem.energetics','Chemical energetics'),('chem.redox','Redox and oxidation numbers'),('chem.equilibria','Equilibria'),('chem.kinetics','Reaction kinetics')]:
    ch(s,i,t,'as','chem-1.md','C1',g)
for i,t in [('chem.lattice','Lattice energy and Born–Haber cycles'),('chem.entropy','Entropy and Gibbs free energy'),('chem.electrochem','Electrochemistry'),('chem.acids2','Acids, bases, buffers and solubility'),('chem.rates2','Rate equations and mechanisms')]:
    ch(s,i,t,'a2','chem-2.md','C2',g)
g='Inorganic chemistry'
for i,t,l in [('chem.periodicity','Periodicity: Period 3','as'),('chem.group2','Group 2','as'),('chem.group17','Group 17: the halogens','as'),('chem.nitrogen','Nitrogen and sulfur','as'),('chem.transition','Transition elements','a2')]:
    ch(s,i,t,l,'chem-2.md','C2',g)
g='Organic chemistry'
for i,t,l in [('chem.org.intro','Introduction to organic chemistry','as'),('chem.org.hydrocarbons','Hydrocarbons: alkanes and alkenes','as'),('chem.org.halogen','Halogenoalkanes','as'),('chem.org.alcohols','Alcohols and phenol','as a2'),('chem.org.carbonyl','Aldehydes and ketones','as'),('chem.org.acids','Carboxylic acids, esters and acyl chlorides','as a2'),('chem.org.arenes','Arenes: benzene and its compounds','a2'),('chem.org.nitrogen','Amines, amides and amino acids','a2'),('chem.org.polymers','Polymerisation','as a2'),('chem.org.synthesis','Organic synthesis','as a2')]:
    ch(s,i,t,l,'chem-3.md','C3',g)
g='Analysis and practical'
ch(s,'chem.analysis','Analytical techniques: IR, mass spectra, NMR and chromatography','as a2','chem-3.md','C3',g)
ch(s,'chem.practical','Practical skills and tests for ions','guide','chem-4.md','C2',g)

s = subj('bio','Biology','Biology','9700',['bio-1.md','bio-2.md','bio-3.md','bio-4.md','bio-5.md'],'From molecules and cells to ecosystems and evolution')
g='Start here'
for i,t,l in [('bio.overview','Biology: the course map','guide'),('bio.f.basics','Biology from zero','pre')]:
    ch(s,i,t,l,'bio-1.md','B1',g)
g='AS Level'
for i,t in [('bio.cells','Cell structure'),('bio.molecules','Biological molecules'),('bio.enzymes','Enzymes'),('bio.membranes','Cell membranes and transport'),('bio.mitosis','The mitotic cell cycle'),('bio.dna','Nucleic acids and protein synthesis')]:
    ch(s,i,t,'as','bio-1.md','B1',g)
for i,t in [('bio.planttransport','Transport in plants'),('bio.mammaltransport','Transport in mammals'),('bio.gasexchange','Gas exchange'),('bio.disease','Infectious diseases'),('bio.immunity','Immunity')]:
    ch(s,i,t,'as','bio-2.md','B2',g)
g='A Level (A2)'
for i,t in [('bio.respiration','Energy and respiration'),('bio.photosynthesis','Photosynthesis')]:
    ch(s,i,t,'a2','bio-3.md','B2',g)
for i,t,l in [('bio.homeostasis','Homeostasis','a2'),('bio.control','Control and coordination','a2'),('bio.inheritance','Inheritance','a2'),('bio.evolution','Selection and evolution','a2'),('bio.classification','Classification, biodiversity and conservation','a2'),('bio.genetech','Genetic technology','a2'),('bio.ecology','Ecosystems and nutrient cycles (UK boards)','a2')]:
    ch(s,i,t,l,'bio-4.md','B3',g)
g='Skills'
for i,t,l in [('bio.stats','Statistics for biologists','as a2'),('bio.practical','Practical skills: microscopy, experiments and planning','guide')]:
    ch(s,i,t,l,'bio-5.md','B2',g)

s = subj('eng','Engineering','Engineering','ENG',['eng-1.md','eng-2.md'],'How Maths and Physics become bridges, engines and circuits')
g='Engineering at A Level'
for i,t,l in [('eng.overview','Engineering: routes and course map','guide'),('eng.what','What engineers actually do','pre')]:
    ch(s,i,t,l,'eng-1.md','E1',g)
g='Engineering foundations'
for i,t,l in [('eng.maths',"The engineer's maths toolkit",'as'),('eng.statics','Statics: forces, moments and structures','as'),('eng.materials','Materials and their properties','as'),('eng.mechanics','Stress, beams and safety factors','a2'),('eng.dynamics','Dynamics and machines','as')]:
    ch(s,i,t,l,'eng-1.md','E1',g)
for i,t,l in [('eng.fluids','Fluid mechanics','a2'),('eng.thermo','Thermodynamics and energy systems','a2'),('eng.electrical','Electrical engineering','as'),('eng.electronics','Electronics and digital systems','as'),('eng.control','Control systems','a2'),('eng.design','Design, drawing and manufacturing','as')]:
    ch(s,i,t,l,'eng-2.md','E2',g)
g='Make it real'
ch(s,'eng.project','Projects, competitions and your next steps','guide','eng-2.md','E2',g)

s = subj('bus','Business','Business','9609',['bus-1.md','bus-2.md','bus-3.md'],'How organisations are run, marketed, staffed and financed')
g='Start here'
for i,t,l in [('bus.overview','Business: the course map','guide'),('bus.f.basics','Business from zero','pre')]:
    ch(s,i,t,l,'bus-1.md','BU1',g)
g='AS Level'
for i,t in [('bus.enterprise','Enterprise'),('bus.structure','Business structure'),('bus.size','Size of business'),('bus.objectives','Business objectives and stakeholders'),('bus.hrm','Human resource management'),('bus.motivation','Motivation'),('bus.management','Management')]:
    ch(s,i,t,'as','bus-1.md','BU1',g)
for i,t in [('bus.marketing','The nature of marketing'),('bus.research','Market research'),('bus.mix','The marketing mix'),('bus.operations','Operations management'),('bus.inventory','Inventory, capacity and outsourcing'),('bus.finance','Business finance and sources of finance'),('bus.cashflow','Cash flow forecasting'),('bus.costs','Costs and break-even analysis'),('bus.budgets','Budgets and variances')]:
    ch(s,i,t,'as','bus-2.md','BU2',g)
g='A Level (A2)'
for i,t in [('bus.external','External influences on business'),('bus.strategy','Business strategy and strategic tools'),('bus.org','Organisational structure and communication'),('bus.leadership','Leadership and HRM strategy'),('bus.marketing2','Marketing analysis and strategy'),('bus.location','Location, scale and quality'),('bus.opsstrategy','Operations strategy and critical path analysis'),('bus.accounts','Financial statements'),('bus.ratios','Ratio analysis'),('bus.investment','Investment appraisal')]:
    ch(s,i,t,'a2','bus-3.md','BU3',g)
g='Skills'
ch(s,'bus.writing','Writing top-band business answers','guide','bus-3.md','BU3',g)

s = subj('econ','Economics and Accounting','Econ & Acc','9708',['econ-1.md','acc-1.md'],'Markets, the economy, and the language of money')
g='Economics'
for i,t,l in [('econ.overview','Economics: the course map','guide'),('econ.basics','The basic economic problem','as'),('econ.demand','Demand, supply and prices','as'),('econ.elasticity','Elasticity','as'),('econ.intervention','Market failure and government intervention','as a2'),('econ.firms','Costs, revenue and market structures','a2'),('econ.labour','Labour markets','a2'),('econ.macro','Measuring the macroeconomy: AD and AS','as'),('econ.growth','Growth, unemployment and inflation','as a2'),('econ.policy','Fiscal, monetary and supply-side policy','as a2'),('econ.trade','Trade, the balance of payments and exchange rates','as a2'),('econ.development','Development and globalisation','a2')]:
    ch(s,i,t,l,'econ-1.md','EC1',g)
g='Accounting'
for i,t,l in [('acc.overview','Accounting: the course map','guide'),('acc.basics','Double-entry bookkeeping','as'),('acc.statements','Preparing financial statements','as a2'),('acc.control','Reconciliations, control accounts and errors','as'),('acc.analysis','Analysing and interpreting accounts','as a2'),('acc.costing','Cost and management accounting','as a2')]:
    ch(s,i,t,l,'acc-1.md','AC1',g)

s = subj('other','Other Subjects','Other','ALL',['other.md'],'Short guides to every other popular A Level')
g='Subject summaries'
for i,t in [('other.overview','All other subjects at a glance'),('other.cs','Computer Science'),('other.english','English Language and Literature'),('other.history','History'),('other.geography','Geography'),('other.psychology','Psychology'),('other.sociology','Sociology'),('other.law','Law'),('other.politics','Politics, Global Perspectives and Thinking Skills'),('other.languages','Modern languages'),('other.arts','Art, Design, Music, Drama and Media'),('other.pe','Physical Education'),('other.humanities','Religious Studies, Philosophy and Classics'),('other.more','Computing, environment and the rest')]:
    ch(s,i,t,'sum','other.md','O1',g)

s = subj('tools','Toolbox','Toolbox','TOOLS',['tools.md','formulas-math.md','formulas-phys.md','formulas-chem.md','formulas-bio.md','formulas-eng.md','formulas-bus.md'],'Formula sheets, calculators, the periodic table and a glossary')
g='Interactive tools'
for i,t in [('tools.grapher','Graph plotter'),('tools.periodic','Periodic table'),('tools.calc','Calculators'),('tools.glossary','Glossary')]:
    ch(s,i,t,'tool','tools.md','ME',g)
g='Formula sheets'
for i,t,f,o in [('tools.f.math','Maths formula sheet','formulas-math.md','M4'),('tools.f.phys','Physics formula and data sheet','formulas-phys.md','P3'),('tools.f.chem','Chemistry data and key equations','formulas-chem.md','C2'),('tools.f.bio','Biology key equations and statistics','formulas-bio.md','B2'),('tools.f.eng','Engineering formula sheet','formulas-eng.md','E2'),('tools.f.bus','Business, economics and accounting formulas','formulas-bus.md','BU3')]:
    ch(s,i,t,'ref',f,o,g)

s = subj('practice','Practice','Practice','QUIZ',['practice.md'],'Mixed quizzes across every subject')
g='Practice'
ch(s,'practice.quiz','Practice quizzes','tool','practice.md','ME',g)

json.dump(dict(subjects=S), open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'src','outline.json'),'w'), indent=1, ensure_ascii=False)
tot = sum(len(x['chapters']) for x in S)
from collections import Counter
print('chapters', tot)
print(Counter(c['owner'] for x in S for c in x['chapters']))

# ---- regenerate OUTLINE.md (compact id list for authors) ----
_R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_o = json.load(open(os.path.join(_R, 'src', 'outline.json')))
_L = ['# Chapter ids (link only to these)', '']
for _s in _o['subjects']:
    _L.append(f"## {_s['title']} (subject id: {_s['id']})"); _g = None
    for _c in _s['chapters']:
        if _c['group'] != _g: _g = _c['group']; _L.append(f"- group: {_g}")
        _L.append(f"  - {_c['id']} — {_c['title']} [{_c['level']}]")
    _L.append('')
if _o.get('aliases'):
    _L += ['## Aliases (old id → chapter that now covers it)', ''] + [f"- {k} → {v}" for k, v in _o['aliases'].items()]
open(os.path.join(_R, 'OUTLINE.md'), 'w').write('\n'.join(_L))
