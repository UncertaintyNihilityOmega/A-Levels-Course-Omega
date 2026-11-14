@chapter cs.development
@title The development life cycle and program design
@level as
@paper CAIE 9618 Paper 2
@time 4–6 hours
@summary Why programs are built in stages, how the waterfall, iterative and rapid application development (RAD) life cycles differ and how to choose one for a scenario, how to design a program with a structure chart and turn the chart into pseudocode, and how a state-transition diagram documents an algorithm.

:::why
Professional programs are not written in one sitting by one person. They are planned, designed, built, tested and kept alive for years by teams, and the way a team organises that work decides whether the program is finished, correct and what the client wanted. Paper 2 asks you to describe these life cycles, to choose one for a scenario, and to design and read the diagrams that programmers use before they write a line of code. The same diagrams make the long pseudocode questions much easier to start.
:::

**Before you start**, you should know how procedures and functions are written, and the difference between passing a parameter by value and by reference, from [Procedures, functions and parameters](#cs.procedures). You should also be comfortable with IF, CASE and loops from [Programming basics: variables, selection and loops](#cs.programming).

:::try Warm-up
Q: What is the difference between a procedure and a function? (from [Procedures, functions and parameters](#cs.procedures))
A: A function returns one value and is used inside an expression, so it is never called with CALL. A procedure does a job and is called with CALL; it can give results back only through BYREF parameters.
Q: A procedure has the header `PROCEDURE Reset(BYREF Count : INTEGER)`. Why is BYREF needed if the procedure sets Count to 0? (from [Procedures, functions and parameters](#cs.procedures))
A: BYREF passes the variable itself, not a copy, so the change reaches the calling program. With BYVAL the procedure would reset only its own copy.
Q: What is the interface of a module? (from [Procedures, functions and parameters](#cs.procedures))
A: Everything another part of the program needs to know to use it: its identifier, the number, order and data types of its parameters, how each is passed, and the type of any return value.
:::

## Why programs need a life cycle

Imagine a bus company in Lima asks you to write a program that plans driver shifts. You could open an editor and start typing. After three weeks you would probably find that you misunderstood what the company needs, that two parts of the program do not fit together, and that nobody knows how to test it. A **development life cycle** is the plan that prevents this: a fixed set of stages that every project passes through, with a clear output from each.

:::def Program development life cycle
The series of stages through which a program passes from the first idea to the end of its working life: analysis, design, coding, testing and maintenance. The stages give the project a structure so it can be planned, managed and checked.
:::

A life cycle helps in four ways.

- **Structure and planning.** Each stage has a purpose and a deliverable, so managers can estimate time and cost and see how far the project has got.
- **Quality.** Checking the work at every stage finds mistakes early. A mistake in the requirements that is found during analysis costs a conversation to fix. The same mistake found after release can mean rewriting a large part of the program.
- **Teamwork.** The documents a stage produces (a requirements specification, a design) are what the next group of people work from, so several programmers can build parts that fit together.
- **Maintenance.** The documents stay behind. A programmer who joins in five years can read why the program works the way it does.

### The five stages

Every life cycle in this chapter contains the same five stages. They differ in how they are ordered, repeated and overlapped.

:::def Analysis
The stage in which the problem is investigated and defined: what the users need the program to do, whether the project is feasible, and what the inputs, processes and outputs must be. Its output is a requirements specification.
:::

:::def Design
The stage in which the solution is planned before any code is written: the modules and how they communicate (a structure chart), the algorithms, the data structures, the screens and reports, and the test plan.
:::

:::def Coding
The stage in which the design is turned into a program in a chosen programming language, following the design and the rules of the language, with comments and meaningful identifiers.
:::

:::def Testing
The stage in which the program is run with test data to find faults and to check it meets the requirements. [Testing, errors and maintenance](#cs.testing) covers the methods in detail.
:::

:::def Maintenance
The stage after the program is released, in which faults are corrected and the program is changed to stay useful.
:::

| Stage | The question it answers | What it produces |
|---|---|---|
| Analysis | What problem must the program solve? | feasibility study, requirements specification |
| Design | How will the program work? | structure chart, algorithms, data structures, interface designs, test plan |
| Coding | How do we write it? | the program code |
| Testing | Does it work, and is it what was asked for? | test results, a corrected program |
| Maintenance | How do we keep it working and useful? | fixes and new versions |

Two terms from analysis are worth knowing. A **feasibility study** asks whether the project can be done at all and whether it is worth doing: is the technology available, will the benefits repay the cost, and can it be finished in time? A **requirements specification** is the document, agreed with the client, that lists exactly what the program must do. Analysts gather the facts for it by interviewing users, giving questionnaires, observing people at work and reading the documents the business already uses.

:::analogy
A life cycle is like building a school. First you decide what the school must hold (analysis), then the architect draws plans (design), then the builders build (coding), inspectors check each part against the plans (testing), and once pupils move in, caretakers repair leaks and add classrooms for years (maintenance). Nobody starts laying bricks before knowing how many classrooms are needed.
:::

:::warn Design is not coding
Students often describe the design stage as "writing the program". Design happens before coding and produces plans, such as structure charts, pseudocode, flowcharts and test plans. The program code is the output of the coding stage.
:::

## The waterfall life cycle

The oldest and simplest way to order the stages is to do them one after another, each finished before the next starts.

:::def Waterfall model
A development life cycle in which the stages (analysis, design, coding, testing, maintenance) are completed in strict order. The output of each stage is the input to the next, and each stage is signed off before the next begins.
:::

:::html
<figure class="fig"><svg viewBox="0 0 540 290" role="img" aria-label="The waterfall model drawn as five boxes stepping down from top left to bottom right: Analysis, Design, Coding, Testing, Maintenance. A downward arrow leads from each stage to the next. A note says each stage is finished and signed off before the next starts."><rect class="fm s-acc sw2" x="10" y="14" width="120" height="34"/><text class="tl tc" x="70" y="35">Analysis</text><rect class="fm s-acc sw2" x="105" y="70" width="120" height="34"/><text class="tl tc" x="165" y="91">Design</text><rect class="fm s-acc sw2" x="200" y="126" width="120" height="34"/><text class="tl tc" x="260" y="147">Coding</text><rect class="fm s-acc sw2" x="295" y="182" width="120" height="34"/><text class="tl tc" x="355" y="203">Testing</text><rect class="fm s-acc sw2" x="390" y="238" width="120" height="34"/><text class="tl tc" x="450" y="259">Maintenance</text><path class="c1 sw2" fill="none" d="M120 48 L120 70" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M215 104 L215 126" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M310 160 L310 182" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M405 216 L405 238" marker-end="url(#ah)"/><text class="tl" x="14" y="200">Each stage is finished and signed off</text><text class="tl" x="14" y="218">before the next stage starts</text></svg><figcaption>The waterfall model. Work flows one way, down the steps, and each stage is signed off before the next begins.</figcaption></figure>
:::

"Signed off" means the client or the project manager has read the stage's documents and formally agreed that they are complete. Only then can the next stage use them. The name comes from the picture: water falls down the steps and does not flow back up.

**Principles.** Plan everything first. Produce a full document at the end of each stage. Do not start coding until the design is complete, and do not start testing until the coding is complete.

**Benefits.**

- The stages and their deliverables are clear, so progress is easy to measure and manage.
- Documentation is thorough, which helps later maintenance and teams that change members.
- It suits projects whose requirements are fully known and will not change, such as a program that follows a published standard or a legal rule.
- Because the design is complete before coding, the programmers know exactly what to build and the cost can be estimated early.

**Drawbacks.**

- A working program appears only near the end, so the client may see it for the first time after months and then discover it is not what they wanted.
- Changing the requirements part-way is expensive, because earlier documents must be redone and signed off again.
- Testing is left until late, so faults that began in the analysis or design are found when they are most costly to fix.
- The user is involved at the start and the end but not in between.

## The iterative life cycle

If a client cannot say exactly what they want until they see something, repeating the stages in short laps is a better plan.

:::def Iterative model
A development life cycle in which the program is built through a series of repeated cycles. Each cycle goes through design, coding and testing for part of the program and ends with a working version that is reviewed, and the feedback shapes the next cycle.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 340 220" role="img" aria-label="The iterative model drawn as a loop of four boxes: Analyse, Design, Code, Test and review, with arrows going round and back to Analyse. The centre says each lap makes a working version."><rect class="fm s-acc sw2" x="10" y="30" width="120" height="34"/><text class="tl tc" x="70" y="51">Analyse</text><rect class="fm s-acc sw2" x="210" y="30" width="120" height="34"/><text class="tl tc" x="270" y="51">Design</text><rect class="fm s-acc sw2" x="210" y="150" width="120" height="34"/><text class="tl tc" x="270" y="171">Code</text><rect class="fm s-acc sw2" x="10" y="150" width="120" height="34"/><text class="tl tc" x="70" y="171">Test and review</text><path class="c1 sw2" fill="none" d="M130 47 L210 47" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M270 64 L270 150" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M210 167 L130 167" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M70 150 L70 64" marker-end="url(#ah)"/><text class="tl tc" x="170" y="100">each lap makes</text><text class="tl tc" x="170" y="122">a working version</text></svg><figcaption>The iterative model. Each lap round the loop produces a working version that users can try, and feedback starts the next lap.</figcaption></figure>
:::

A first lap might build only the core of the program: for a shift planner, enter drivers and print one day's shifts. The users try it and say what is missing. The second lap adds weekly planning, the third adds holiday requests, and so on until the program is complete.

**Principles.** Start with a small working version, not a finished design. Repeat design, coding and testing, adding or improving something each time. Use the feedback from each version to decide what to do next.

**Benefits.**

- A working version exists early, so users can try it and the client sees real progress.
- Changing requirements are expected and absorbed in the next lap, rather than breaking a signed-off plan.
- Faults are found and fixed in small pieces, because each lap is tested.
- The riskiest parts can be built first, so a hard problem shows up early.

**Drawbacks.**

- It is hard to say at the start how many laps are needed, so cost and finishing date are uncertain.
- Without care the program grows in an unplanned way, and the structure can become untidy.
- It needs the client or users to give feedback after every lap.
- Documentation may be thinner or out of date because the design keeps changing.

## Rapid application development (RAD)

RAD takes the iterative idea and pushes speed and user involvement to the limit.

:::def Prototype
A working but incomplete early version of a program, built quickly to show users and collect their feedback. A prototype may be thrown away or developed into the final program.
:::

:::def Rapid application development (RAD)
A development life cycle that builds a series of prototypes quickly, with users involved throughout. Each prototype is shown to the users, their feedback is used to improve the next one, and the work is done in short fixed time periods using existing components wherever possible.
:::

The principles of RAD are:

- **prototypes** are built early and often, with the screens users will actually see;
- **users take part** in the project all the way through, testing each prototype and saying what to change;
- work is **time-boxed**: each cycle has a fixed short length, and what cannot be finished is dropped or postponed rather than delaying the cycle;
- **reuse** of existing code, libraries and design tools replaces writing everything from scratch.

**Benefits.**

- A usable program is delivered quickly, so the client gets value early.
- Because users shape every prototype, the final program is more likely to match what they need and they accept it more readily.
- Changing requirements are welcome, and mistakes in understanding are caught early.
- Reusing components saves time and cost.

**Drawbacks.**

- It needs users or the client to be available often, and the project suffers if they are not.
- Less up-front planning and documentation can produce a program that is poorly structured and hard to maintain.
- The fixed time boxes can squeeze testing and quality.
- It is not suited to large or safety-critical systems, where the requirements must be complete and proved before anything is built.

:::warn RAD is not "no planning"
A common wrong answer says RAD means the programmers just start coding without a design. RAD still has analysis, design and testing in each cycle. What changes is that they are short, informal and repeated, and that users are involved. Never write "no design" as a feature of RAD.
:::

### Iterative or RAD?

The two are close, so examiners accept a clear description of either for a changing-requirements scenario. If you need to tell them apart: an iterative life cycle builds the real program in repeated laps, each adding a piece. RAD stresses fast **prototypes** shown to the **users** in fixed **time boxes**, with **reused components**.

## Choosing a life cycle

There is no best life cycle. The choice depends on how well the requirements are known, how likely they are to change, the size and risk of the project and how much the users can take part.

| | Waterfall | Iterative | RAD |
|---|---|---|---|
| Requirements | known and fixed at the start | become clear as the program grows | unclear or changing |
| First working version | near the end | after the first lap | after the first prototype, quickly |
| User involvement | start and end | at the end of each lap | all the way through |
| Documentation | thorough | moderate | light |
| Cost of changing requirements | high | low | low |
| Best for | large or safety-critical projects with fixed requirements | medium projects that grow in stages | small interactive programs with changing needs |

:::exam Choosing and justifying a life cycle
Name the life cycle first, then give reasons taken from the scenario, not from a list you learned. "Waterfall, because the requirements for the flight-control program are fixed by safety rules and every stage must be documented and signed off before the next" earns marks. "Waterfall, because it has stages" does not.
:::

:::eg Choosing a life cycle for a scenario (exam style)
A start-up in Medellín is developing a mobile app for ordering food from local restaurants. The owner has a rough idea of the screens but expects to change many features after watching customers use it. The team has five programmers and wants to release something within two months.

(a) State a suitable life cycle for the app. [1 mark]

(b) Give two benefits and one drawback of this life cycle for this project. [3 marks]

**(a)** Rapid application development (RAD). Iterative is also accepted. [B1]

**(b)** Choose benefits that fit the scenario, and a drawback that could really happen to it.

- Benefit: a prototype is ready quickly, so the app can be released within the two months and customers can start using it. [B1]
- Benefit: customers' reactions are used to change the next prototype, so the requirements the owner is unsure about are settled by real use. [B1]
- Drawback: it needs the owner and customers to give feedback constantly, and with little documentation the code may be hard to maintain later. [B1]

A drawback must be a real weakness. "It is quick" is a benefit, and "it takes a long time" would be wrong for RAD.
:::

:::eg Matching life cycles to projects
For each project, name the most suitable life cycle and give one reason.

1. The control program for a railway signalling system, with requirements fixed by national safety rules.
2. A school's new timetable program. The head of department can describe the first version but expects to ask for changes as staff use it.
3. A tool a bank must update by a fixed legal date. The law's requirements are published in full and will not change before that date.

**1.** Waterfall. The requirements are fixed and failure is dangerous, so complete documentation, thorough testing and sign-off at every stage matter more than speed. [B1] [B1]

**2.** Iterative (or RAD). The staff can try each version and say what to change, and the requirements will change. [B1] [B1]

**3.** Waterfall. The requirements are known in full and fixed, so planning everything in advance is efficient. [B1] [B1]
:::

:::tip Life cycles can be mixed
Real projects often mix them: a team might use waterfall for the part that controls hardware, where the specification is fixed, and RAD for the screens, where the users' opinions matter. In an exam, choose the one that fits the scenario best and say why.
:::

## Program design: decomposition and structure charts

Large problems are solved by **decomposition**: breaking the problem into smaller sub-tasks until each is simple enough to write as one procedure or function. The result is a set of **modules**, each with one job. You met modules in [Procedures, functions and parameters](#cs.procedures). A structure chart is the diagram of that decomposition.

:::def Structure chart
A diagram of a program design that shows how a problem is decomposed into modules (procedures and functions) arranged in a hierarchy, which module calls which, and the data and flags passed between modules.
:::

The purpose of a structure chart is to plan the program before coding. It shows the programmer which modules to write, what each needs to be given and what it must give back. It also lets a team split the work, because the parameters between the modules are agreed in the chart.

### How to read a structure chart

:::html
<figure class="fig"><svg viewBox="0 0 600 430" role="img" aria-label="A structure chart. The top module ProcessParcel calls three modules: GetParcel, CalculateCharge and PrintReceipt. GetParcel passes up Mass and Zone as data and Valid as a flag. CalculateCharge receives Mass and Zone and passes up Charge. PrintReceipt receives Mass, Zone and Charge. CalculateCharge calls BaseRate, which receives Zone and passes up Rate, and Surcharge, which receives Mass and passes up Extra. An open circle at the tail of an arrow marks data and a filled circle marks a flag."><text class="tl" x="10" y="26">open circle: data couple</text><text class="tl" x="10" y="44">filled circle: flag</text><rect class="fm s-acc sw2" x="230" y="20" width="140" height="34"/><text class="tl tc" x="300" y="41">ProcessParcel</text><rect class="fm s-acc sw2" x="40" y="200" width="110" height="34"/><text class="tl tc" x="95" y="221">GetParcel</text><rect class="fm s-acc sw2" x="230" y="200" width="140" height="34"/><text class="tl tc" x="300" y="221">CalculateCharge</text><rect class="fm s-acc sw2" x="445" y="200" width="120" height="34"/><text class="tl tc" x="505" y="221">PrintReceipt</text><path class="ln" fill="none" d="M300 54 L300 84"/><path class="ln" fill="none" d="M95 84 L505 84"/><path class="ln" fill="none" d="M95 84 L95 200"/><path class="ln" fill="none" d="M505 84 L505 200"/><path class="ln" fill="none" d="M300 84 L300 200"/><path class="c1" fill="none" d="M109 120 L109 96" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="109" cy="120" r="3.5"/><text class="tl" x="117" y="112">Mass</text><path class="c1" fill="none" d="M109 154 L109 130" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="109" cy="154" r="3.5"/><text class="tl" x="117" y="146">Zone</text><path class="c1" fill="none" d="M109 188 L109 164" marker-end="url(#ah)"/><circle class="fi" cx="109" cy="188" r="3.5"/><text class="tl" x="117" y="180">Valid</text><path class="c1" fill="none" d="M286 113 L286 137" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="286" cy="113" r="3.5"/><text class="tl te" x="278" y="129">Mass</text><path class="c1" fill="none" d="M286 147 L286 171" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="286" cy="147" r="3.5"/><text class="tl te" x="278" y="163">Zone</text><path class="c1" fill="none" d="M314 154 L314 130" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="314" cy="154" r="3.5"/><text class="tl" x="322" y="146">Charge</text><path class="c1" fill="none" d="M491 96 L491 120" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="491" cy="96" r="3.5"/><text class="tl te" x="483" y="112">Mass</text><path class="c1" fill="none" d="M491 130 L491 154" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="491" cy="130" r="3.5"/><text class="tl te" x="483" y="146">Zone</text><path class="c1" fill="none" d="M491 164 L491 188" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="491" cy="164" r="3.5"/><text class="tl te" x="483" y="180">Charge</text><rect class="fm s-acc sw2" x="165" y="380" width="110" height="34"/><text class="tl tc" x="220" y="401">BaseRate</text><rect class="fm s-acc sw2" x="320" y="380" width="120" height="34"/><text class="tl tc" x="380" y="401">Surcharge</text><path class="ln" fill="none" d="M300 234 L300 264"/><path class="ln" fill="none" d="M220 264 L380 264"/><path class="ln" fill="none" d="M220 264 L220 380"/><path class="ln" fill="none" d="M380 264 L380 380"/><path class="c1" fill="none" d="M206 310 L206 334" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="206" cy="310" r="3.5"/><text class="tl te" x="198" y="326">Zone</text><path class="c1" fill="none" d="M234 334 L234 310" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="234" cy="334" r="3.5"/><text class="tl" x="242" y="326">Rate</text><path class="c1" fill="none" d="M366 310 L366 334" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="366" cy="310" r="3.5"/><text class="tl te" x="358" y="326">Mass</text><path class="c1" fill="none" d="M394 334 L394 310" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="394" cy="334" r="3.5"/><text class="tl" x="402" y="326">Extra</text></svg><figcaption>Structure chart for the parcel program. Arrows show data passed between modules, not the order of execution: open circle for data, filled circle for a flag.</figcaption></figure>
:::

A delivery company in Accra charges for each parcel by its mass and delivery zone. The program reads the details of a parcel, checks them, works out the charge and prints a receipt. The chart above decomposes it. Read it from the top.

- **A box is a module**: a procedure or a function, named on the box. The top box is the main task, here called ProcessParcel.
- **A line from a box down to another means "calls"**: ProcessParcel calls GetParcel, CalculateCharge and PrintReceipt, and CalculateCharge calls BaseRate and Surcharge. Modules on the same row are normally drawn in the order they are called, from left to right.
- **An arrow beside a line is a parameter**, a piece of data passed between the two modules. The arrow's **direction** tells you which way it goes: an arrow pointing **down** is passed **into** the lower module from the module that calls it, and an arrow pointing **up** is passed **back** to the calling module.
- **The label** on an arrow is the name of the parameter.

:::def Data couple
An item of data passed between two modules, drawn as an arrow, labelled with the data's name, with an open circle at its tail.
:::

:::def Flag
An item of control information passed between modules, such as whether a value is valid or a search found its target, drawn as an arrow with a filled circle at its tail. A flag usually has the data type BOOLEAN.
:::

In the parcel chart, GetParcel sends Mass and Zone up to its caller, and a flag, Valid, which says whether the user's entry passed the checks. CalculateCharge is given Mass and Zone and sends Charge up. PrintReceipt is given three items and sends nothing back, because it only prints.

:::warn Arrows show data, not the order of execution
The arrows in a structure chart show **what data passes where**. They do not show the order in which the modules run, and a chart contains no decisions or loops by itself (the two symbols below add those). To see the order, read the modules left to right, or look at the main program in the pseudocode.
:::

### Selection and iteration in a structure chart

Two more symbols show when modules are called.

:::html
<figure class="fig"><svg viewBox="0 0 600 200" role="img" aria-label="Two small structure charts side by side. Left, iteration: module Main calls Read and Show, and a curved arrow across the two lines means they repeat. Right, selection: module Menu has a diamond under it and calls Add or Delete, meaning one of them is chosen."><text class="tl tc" x="150" y="16">Iteration: repeat</text><text class="tl tc" x="450" y="16">Selection: choose one</text><rect class="fm s-acc sw2" x="100" y="30" width="100" height="34"/><text class="tl tc" x="150" y="51">Main</text><path class="ln" fill="none" d="M150 64 L150 90"/><path class="ln" fill="none" d="M60 90 L240 90"/><rect class="fm s-acc sw2" x="15" y="140" width="90" height="34"/><text class="tl tc" x="60" y="161">Read</text><rect class="fm s-acc sw2" x="195" y="140" width="90" height="34"/><text class="tl tc" x="240" y="161">Show</text><path class="ln" fill="none" d="M60 90 L60 140"/><path class="ln" fill="none" d="M240 90 L240 140"/><path class="c1 sw2" fill="none" d="M46 112 Q150 142 254 112" marker-end="url(#ah)"/><rect class="fm s-acc sw2" x="400" y="30" width="100" height="34"/><text class="tl tc" x="450" y="51">Menu</text><polygon class="fp s-acc sw2" points="450,64 460,74 450,84 440,74"/><path class="ln" fill="none" d="M450 84 L450 100"/><path class="ln" fill="none" d="M360 100 L540 100"/><rect class="fm s-acc sw2" x="315" y="140" width="90" height="34"/><text class="tl tc" x="360" y="161">Add</text><rect class="fm s-acc sw2" x="495" y="140" width="90" height="34"/><text class="tl tc" x="540" y="161">Delete</text><path class="ln" fill="none" d="M360 100 L360 140"/><path class="ln" fill="none" d="M540 100 L540 140"/><path class="ln-m thin dash" fill="none" d="M300 24 L300 190"/></svg><figcaption>The two control symbols. A curved arrow across the lines means the modules below repeat; a diamond means one of them is chosen.</figcaption></figure>
:::

- A **curved arrow** across the lines to some modules means **iteration**: those modules are called repeatedly, as in a loop. In the left chart, Main calls Read and Show again and again.
- A **diamond** on a module's lower edge means **selection**: the module calls only one of the modules below it, chosen by a condition. In the right chart, Menu calls Add or Delete, not both.

The parcel chart leaves out the diamond to keep the figure readable. In the program that follows, CalculateCharge and PrintReceipt are called only when Valid is TRUE, which a fuller chart would show with a diamond under ProcessParcel.

:::key Reading and drawing a structure chart
- Box = module (procedure or function). Line = "calls". Top box = the whole task.
- Arrow pointing **down** = data passed **into** the lower module. Arrow pointing **up** = data **returned** to the module above.
- Open circle at the tail = **data couple**. Filled circle at the tail = **flag**.
- Curved arrow across the lines = **iteration**. Diamond = **selection**.
- Label every arrow with the parameter's name, and give each module one clear job.
:::

### From structure chart to pseudocode

A structure chart contains the interface of every module, so you can write each module's header from it.

- A box with arrows pointing **down** into it has **parameters**.
- A box with an arrow pointing **up** out of it **returns** that item. If it returns exactly one item, a **function** is the natural choice, with `RETURNS` and a type. If it returns several items or none, a **procedure** is used, and each returned item is a **BYREF** parameter.
- A parameter that is only passed down is **BYVAL**. A parameter that is passed up (or both ways) is **BYREF**, if the module is a procedure. A function never uses BYREF.
- A flag is usually a BOOLEAN parameter or the BOOLEAN returned by a function.

The data types are not in the chart. You choose them from the problem: Mass is REAL, Zone is a single letter so CHAR, Valid is BOOLEAN.

:::eg Writing the modules of the parcel chart
The delivery company in Accra charges 5.0 per kg in zone A, 8.0 per kg in zone B and 12.0 per kg in zone C. A parcel over 25.0 kg pays a surcharge of 3.0. A parcel is valid if its mass is greater than 0.0 and its zone is A, B or C. Write the pseudocode for the modules in the structure chart and for ProcessParcel, which outputs a receipt for a valid parcel.

Take the modules from the bottom up, deriving each header from its arrows.

- GetParcel has three arrows pointing up and none down, so it is a **procedure** with three **BYREF** parameters: Mass, Zone and the flag Valid.
- BaseRate receives Zone and returns Rate, so it is a **function** with one parameter and `RETURNS REAL`.
- Surcharge receives Mass and returns Extra, so it is a **function** `RETURNS REAL`.
- CalculateCharge receives Mass and Zone and returns Charge, so it is a **function** with two parameters that calls the other two.
- PrintReceipt receives three items and returns none, so it is a **procedure** with three BYVAL parameters.

```pseudocode
PROCEDURE GetParcel(BYREF Mass : REAL, BYREF Zone : CHAR, BYREF Valid : BOOLEAN)
   OUTPUT "Enter the mass in kg"
   INPUT Mass
   OUTPUT "Enter the zone (A, B or C)"
   INPUT Zone
   Valid ← Mass > 0.0 AND (Zone = 'A' OR Zone = 'B' OR Zone = 'C')
ENDPROCEDURE

FUNCTION BaseRate(Zone : CHAR) RETURNS REAL
   CASE OF Zone
      'A' : RETURN 5.0
      'B' : RETURN 8.0
      'C' : RETURN 12.0
      OTHERWISE : RETURN 0.0
   ENDCASE
ENDFUNCTION

FUNCTION Surcharge(Mass : REAL) RETURNS REAL
   IF Mass > 25.0 THEN
      RETURN 3.0
   ELSE
      RETURN 0.0
   ENDIF
ENDFUNCTION

FUNCTION CalculateCharge(Mass : REAL, Zone : CHAR) RETURNS REAL
   RETURN Mass * BaseRate(Zone) + Surcharge(Mass)
ENDFUNCTION

PROCEDURE PrintReceipt(Mass : REAL, Zone : CHAR, Charge : REAL)
   OUTPUT "Mass: ", Mass, " kg, zone ", Zone
   OUTPUT "Charge: ", Charge
ENDPROCEDURE
```

The main module calls them in the order of the chart and uses the flag to decide whether to carry on.

```pseudocode
DECLARE Mass, Charge : REAL
DECLARE Zone : CHAR
DECLARE Valid : BOOLEAN

CALL GetParcel(Mass, Zone, Valid)
IF Valid = TRUE THEN
   Charge ← CalculateCharge(Mass, Zone)
   CALL PrintReceipt(Mass, Zone, Charge)
ELSE
   OUTPUT "Invalid parcel"
ENDIF
```

Mark points:

- GetParcel is a procedure with three BYREF parameters (Mass, Zone, Valid) [B1]
- BaseRate and Surcharge are functions that RETURN a REAL, with parameters passed by value [B1]
- CalculateCharge is a function with parameters Mass and Zone that calls BaseRate and Surcharge and returns the charge [B1]
- PrintReceipt is a procedure whose parameters are all by value [B1]
- main program calls the modules in the order of the chart, using CALL for procedures but not for functions [B1]
- the flag Valid is tested before the charge is calculated [B1]

A 30.0 kg parcel to zone B costs \(30.0 \times 8.0 + 3.0 = 243.0\).
:::

The same design in Python. A Python function can return several values, so `get_parcel` returns Mass, Zone and Valid together instead of using BYREF (see [Procedures, functions and parameters](#cs.procedures)). The program below reads 30 and B as input.

```python
def get_parcel():
    mass = float(input("Enter the mass in kg: "))
    zone = input("Enter the zone (A, B or C): ")
    valid = mass > 0 and zone in ("A", "B", "C")
    return mass, zone, valid


def base_rate(zone):
    rates = {"A": 5.0, "B": 8.0, "C": 12.0}
    return rates.get(zone, 0.0)


def surcharge(mass):
    if mass > 25:
        return 3.0
    return 0.0


def calculate_charge(mass, zone):
    return mass * base_rate(zone) + surcharge(mass)


def print_receipt(mass, zone, charge):
    print("Mass:", mass, "kg, zone", zone)
    print("Charge:", charge)


mass, zone, valid = get_parcel()
if valid:
    charge = calculate_charge(mass, zone)
    print_receipt(mass, zone, charge)
else:
    print("Invalid parcel")
```

Output, when the user types 30 and B:

```output
Enter the mass in kg: 30
Enter the zone (A, B or C): B
Mass: 30.0 kg, zone B
Charge: 243.0
```

### Drawing a structure chart for a problem

To construct a chart from a description, follow these steps.

:::steps
1. Name the whole task in the top box.
2. List the sub-tasks it needs, usually input, processing and output, and give each its own box. A box that is still too big is split again.
3. Order the boxes on each row in the order they run.
4. For each module, decide what it must be given and what it must give back, and draw an arrow for each, down for "given" and up for "returned", using a filled circle for a flag.
5. Check that every item a module needs is either passed down to it or returned by a module that runs before it.
:::

:::eg Constructing a structure chart (exam style)
Four friends in Cairo share a restaurant bill equally. A program reads the total bill and the number of people, calculates what each person pays and outputs it. Draw a structure chart for the program, showing the parameters passed between modules. [4 marks]

The three jobs are input, calculation and output, so the top module has three modules below it, left to right in the order they run. Then decide what moves between them: GetBill produces Total and People, CalculateShare needs both and produces Share, and ShowShare needs only Share.

:::html
<figure class="fig"><svg viewBox="0 0 520 250" role="img" aria-label="A structure chart. The top module SplitBill calls three modules. GetBill passes up Total and People. CalculateShare receives Total and People and passes up Share. ShowShare receives Share. All are data couples, drawn with an open circle at the tail of each arrow."><text class="tl" x="10" y="26">open circle: data couple</text><text class="tl" x="10" y="44">filled circle: flag</text><rect class="fm s-acc sw2" x="200" y="20" width="120" height="34"/><text class="tl tc" x="260" y="41">SplitBill</text><path class="ln" fill="none" d="M260 54 L260 80"/><path class="ln" fill="none" d="M90 80 L430 80"/><rect class="fm s-acc sw2" x="35" y="170" width="110" height="34"/><text class="tl tc" x="90" y="191">GetBill</text><path class="ln" fill="none" d="M90 80 L90 170"/><path class="c1" fill="none" d="M104 120 L104 96" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="104" cy="120" r="3.5"/><text class="tl" x="112" y="112">Total</text><path class="c1" fill="none" d="M104 154 L104 130" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="104" cy="154" r="3.5"/><text class="tl" x="112" y="146">People</text><rect class="fm s-acc sw2" x="185" y="170" width="150" height="34"/><text class="tl tc" x="260" y="191">CalculateShare</text><path class="ln" fill="none" d="M260 80 L260 170"/><path class="c1" fill="none" d="M246 96 L246 120" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="246" cy="96" r="3.5"/><text class="tl te" x="238" y="112">Total</text><path class="c1" fill="none" d="M246 130 L246 154" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="246" cy="130" r="3.5"/><text class="tl te" x="238" y="146">People</text><path class="c1" fill="none" d="M274 137 L274 113" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="274" cy="137" r="3.5"/><text class="tl" x="282" y="129">Share</text><rect class="fm s-acc sw2" x="375" y="170" width="110" height="34"/><text class="tl tc" x="430" y="191">ShowShare</text><path class="ln" fill="none" d="M430 80 L430 170"/><path class="c1" fill="none" d="M416 113 L416 137" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="416" cy="113" r="3.5"/><text class="tl te" x="408" y="129">Share</text></svg><figcaption>Structure chart for the bill-sharing program: every couple is data, so every arrow has an open circle.</figcaption></figure>
:::

Mark points:

- a top module with three modules below it for input, calculation and output, in that order [B1]
- GetBill with Total and People passed up to the calling module [B1]
- CalculateShare with Total and People passed down and Share passed up [B1]
- ShowShare with Share passed down, and every arrow labelled and pointing in the correct direction [B1]

In pseudocode, GetBill has two BYREF parameters, CalculateShare is a function with two parameters that returns the share, and ShowShare has one BYVAL parameter.
:::

The program for the bill-sharing chart, in Python. The user types 90 and 4.

```python
def get_bill():
    total = float(input("Enter the total bill: "))
    people = int(input("Enter the number of people: "))
    return total, people


def calculate_share(total, people):
    return total / people


def show_share(share):
    print("Each person pays:", share)


total, people = get_bill()
show_share(calculate_share(total, people))
```

Output, when the user types 90 and 4:

```output
Enter the total bill: 90
Enter the number of people: 4
Each person pays: 22.5
```

:::exam Marks for structure charts
Examiners look for four things: modules in a sensible hierarchy, every module with one clear job, every parameter shown as an arrow with a label, and arrows pointing the right way. Do not draw arrows for the order of execution, and do not put code inside the boxes.
:::

## State-transition diagrams

A structure chart shows the parts of a program. Some algorithms are better described by what **state** they are in and what makes them change state. A turnstile is locked or unlocked. A cash machine is waiting for a first PIN, a second PIN, or has accepted or blocked a card. A state-transition diagram documents that behaviour.

:::def State
A condition that a system or algorithm can be in at one time, which determines how it responds to an event. A system is in exactly one state at a time.
:::

:::def State-transition diagram
A diagram that documents an algorithm or system by showing its states as circles and the transitions between them as arrows. Each arrow is labelled with the event that causes the transition and the action taken, written event / action.
:::

:::html
<figure class="fig small"><svg viewBox="0 0 440 198" role="img" aria-label="A state-transition diagram of a turnstile with two states, Locked and Unlocked. A start arrow points at Locked. The arrow from Locked to Unlocked is labelled coin slash unlock. The arrow from Unlocked back to Locked is labelled push slash lock. Locked has a loop labelled push slash nothing and Unlocked has a loop labelled coin slash nothing."><circle class="fm s-acc sw2" cx="120" cy="120" r="36"/><text class="tl tc" x="120" y="124">Locked</text><circle class="fm s-acc sw2" cx="330" cy="120" r="36"/><text class="tl tc" x="330" y="124">Unlocked</text><path class="c1 sw2" fill="none" d="M20 120 L83 120" marker-end="url(#ah)"/><text class="tl" x="14" y="104">start</text><path class="c1 sw2" fill="none" d="M148 96 Q225 62 302 96" marker-end="url(#ah)"/><text class="tl tc" x="225" y="70">coin / unlock</text><path class="c1 sw2" fill="none" d="M302 144 Q225 176 148 144" marker-end="url(#ah)"/><text class="tl tc" x="225" y="187">push / lock</text><path class="c1 sw2" fill="none" d="M98 90 C50 20 130 20 122 83" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M328 83 C320 20 400 20 352 90" marker-end="url(#ah)"/><text class="tl tc" x="80" y="20">push / nothing</text><text class="tl tc" x="370" y="20">coin / nothing</text></svg><figcaption>A turnstile has two states. Each arrow is labelled event / action, and an arrow that returns to its own state is a loop.</figcaption></figure>
:::

The turnstile in the figure shows all the parts of the notation.

- A **circle** is a state, named inside it.
- An **arrow** between two circles is a **transition**: the system moves from the state at its tail to the state at its head. The label is **event / action**. The event is what happens (a coin is inserted, a button is pressed). The action is what the system does in response (unlock the gate). If nothing is done, write "nothing" or leave the action out.
- A **start arrow** from nowhere points at the **start state**, where the system begins.
- An arrow that leaves a state and returns to the **same state** is a **loop**: the event does not change the state.
- A state drawn as a **double circle** is a **stop** (final) state, where the algorithm ends.

The same information fits in a table, the **state-transition table**, with one row for each transition. It is useful because it is complete: every state is listed against every event.

| Current state | Event | Next state | Action |
|---|---|---|---|
| Locked | coin | Unlocked | unlock the gate |
| Locked | push | Locked | nothing |
| Unlocked | push | Locked | lock the gate |
| Unlocked | coin | Unlocked | nothing |

:::warn Every event from every state
A diagram is complete only if every state has an arrow for every event the scenario mentions. A student who forgets that pushing a locked turnstile does nothing, or that a second coin in the Unlocked state changes nothing, has an incomplete diagram. Check each circle: does it have one outgoing arrow for each event?
:::

### A worked example: a PIN check

A cash machine gives a customer three tries to enter the correct PIN. A correct PIN shows the menu and ends the check. After a third wrong PIN the machine keeps the card and the check ends.

:::html
<figure class="fig"><svg viewBox="0 0 520 445" role="img" aria-label="A state-transition diagram for a PIN check at a cash machine. States: Try 1, Try 2, Try 3, Accepted and Blocked. Accepted and Blocked are drawn as double circles because they are stop states. From each Try state, a correct PIN leads to Accepted with the action menu. A wrong PIN leads from Try 1 to Try 2 and from Try 2 to Try 3, with the action try again, and from Try 3 to Blocked with the action keep card."><circle class="fm s-acc sw2" cx="80" cy="50" r="32"/><text class="tl tc" x="80" y="54">Try 1</text><circle class="fm s-acc sw2" cx="80" cy="160" r="32"/><text class="tl tc" x="80" y="164">Try 2</text><circle class="fm s-acc sw2" cx="80" cy="270" r="32"/><text class="tl tc" x="80" y="274">Try 3</text><circle class="fm s-acc sw2" cx="80" cy="390" r="40"/><circle class="ln" fill="none" cx="80" cy="390" r="34"/><text class="tl tc" x="80" y="394">Blocked</text><circle class="fm s-acc sw2" cx="430" cy="160" r="40"/><circle class="ln" fill="none" cx="430" cy="160" r="34"/><text class="tl tc" x="430" y="164">Accepted</text><path class="c1 sw2" fill="none" d="M10 50 L47 50" marker-end="url(#ah)"/><text class="tl" x="10" y="34">start</text><path class="c1 sw2" fill="none" d="M80 83 L80 127" marker-end="url(#ah)"/><text class="tl" x="92" y="99">wrong PIN</text><text class="tl" x="92" y="121">try again</text><path class="c1 sw2" fill="none" d="M80 193 L80 237" marker-end="url(#ah)"/><text class="tl" x="92" y="209">wrong PIN</text><text class="tl" x="92" y="231">try again</text><path class="c1 sw2" fill="none" d="M80 303 L80 349" marker-end="url(#ah)"/><text class="tl" x="92" y="320">wrong PIN</text><text class="tl" x="92" y="342">keep card</text><path class="c1 sw2" fill="none" d="M111.482 59.8943 L390.886 147.707" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M113 160 L389 160" marker-end="url(#ah)"/><path class="c1 sw2" fill="none" d="M111.482 260.106 L390.886 172.293" marker-end="url(#ah)"/><text class="tl tc" x="330" y="100">correct PIN / menu</text><text class="tl tc" x="255" y="150">correct PIN / menu</text><text class="tl tc" x="330" y="232">correct PIN / menu</text></svg><figcaption>The PIN check. Double circles are stop states. Every Try state has one arrow for each event: correct PIN and wrong PIN.</figcaption></figure>
:::

The diagram has five states and six transitions, which the table lists.

| Current state | Event | Next state | Action |
|---|---|---|---|
| Try1 | correct | Accepted | Menu |
| Try1 | wrong | Try2 | Try again |
| Try2 | correct | Accepted | Menu |
| Try2 | wrong | Try3 | Try again |
| Try3 | correct | Accepted | Menu |
| Try3 | wrong | Blocked | Keep card |

(The states are written without spaces, Try1, in the table and the code, because identifiers cannot contain spaces.)

### From diagram to pseudocode

A state-transition diagram turns directly into a loop that keeps the current state in a variable. Each time round the loop, the program reads an event, looks at the current state with a CASE statement, performs the action and sets the next state. The loop stops when the state is a stop state.

:::key Turning a state-transition diagram into pseudocode
1. A variable (here State) holds the current state. Set it to the start state before the loop.
2. The loop runs until State is a stop state (REPEAT … UNTIL, or WHILE).
3. In the loop, read the event, then CASE OF State selects the state's code.
4. Inside each case, an IF on the event performs the action and assigns the next state.
5. A state with no arrow for an event does nothing for that event: no code is needed.
:::

```pseudocode
DECLARE State, Event : STRING
State ← "Try1"
REPEAT
   INPUT Event
   CASE OF State
      "Try1" :
         IF Event = "correct" THEN
            OUTPUT "Menu"
            State ← "Accepted"
         ELSE
            OUTPUT "Try again"
            State ← "Try2"
         ENDIF
      "Try2" :
         IF Event = "correct" THEN
            OUTPUT "Menu"
            State ← "Accepted"
         ELSE
            OUTPUT "Try again"
            State ← "Try3"
         ENDIF
      "Try3" :
         IF Event = "correct" THEN
            OUTPUT "Menu"
            State ← "Accepted"
         ELSE
            OUTPUT "Keep card"
            State ← "Blocked"
         ENDIF
   ENDCASE
UNTIL State = "Accepted" OR State = "Blocked"
```

Here the events are the words correct and wrong, which in a real machine come from comparing the typed PIN with the stored one. Suppose the user's events are wrong, wrong, correct. A trace table records the state after each event.

| Event | State | OUTPUT |
|---|---|---|
| | Try1 | |
| wrong | Try2 | Try again |
| wrong | Try3 | Try again |
| correct | Accepted | Menu |

With wrong, wrong, wrong the output would be Try again, Try again, Keep card and the final state Blocked.

Python can store the table itself as a dictionary whose keys are (state, event) pairs. The loop is then the same for every state, and a different state machine needs only a different table.

```python
transitions = {
    ("Try1", "correct"): ("Accepted", "Menu"),
    ("Try1", "wrong"): ("Try2", "Try again"),
    ("Try2", "correct"): ("Accepted", "Menu"),
    ("Try2", "wrong"): ("Try3", "Try again"),
    ("Try3", "correct"): ("Accepted", "Menu"),
    ("Try3", "wrong"): ("Blocked", "Keep card"),
}
events = ["wrong", "wrong", "wrong"]
state = "Try1"
position = 0
while state != "Accepted" and state != "Blocked":
    event = events[position]
    position = position + 1
    state, action = transitions[(state, event)]
    print(event, "->", state, "|", action)
```

Output:

```output
wrong -> Try2 | Try again
wrong -> Try3 | Try again
wrong -> Blocked | Keep card
```

:::eg Completing a state-transition table (exam style)
A drinks machine in a school in Kampala sells one drink for two coins. It starts with no credit. When a coin is inserted it shows the credit. When the second coin is inserted it releases a drink and returns to no credit. If the refund button is pressed with one coin inside, the coin is returned and the machine goes back to no credit. Pressing refund with no credit does nothing.

Complete the state-transition table. [4 marks]

| Current state | Event | Next state | Action |
|---|---|---|---|
| NoCredit | coin | OneCoin | show credit |
| NoCredit | refund | | |
| OneCoin | coin | | |
| OneCoin | refund | | |

The machine has two states, NoCredit (the start state) and OneCoin. Take each blank row in turn and decide what the description says.

| Current state | Event | Next state | Action |
|---|---|---|---|
| NoCredit | coin | OneCoin | show credit |
| NoCredit | refund | NoCredit | nothing |
| OneCoin | coin | NoCredit | release drink |
| OneCoin | refund | NoCredit | return coin |

Mark points:

- NoCredit with refund: next state NoCredit and no action [B1]
- OneCoin with coin: next state NoCredit [B1]
- OneCoin with coin: action release a drink [B1]
- OneCoin with refund: next state NoCredit and action return the coin [B1]
:::

## Spot the error, try it yourself and exam practice

:::eg Spot the error: a function header from a structure chart
Question: In a structure chart, the module Surcharge has one arrow pointing down into it, labelled Mass (data), and one arrow pointing up out of it, labelled Extra (data). Mass is a REAL. Write the pseudocode for Surcharge, which returns 3.0 when Mass is over 25.0 and 0.0 otherwise. [4 marks]

A student wrote:

```pseudocode
01  FUNCTION Surcharge(BYREF Mass : REAL) RETURNS REAL
02     IF Mass > 25.0 THEN
03        RETURN 3.0
04     ELSE
05        RETURN 0.0
06     ENDIF
07  ENDFUNCTION
```

The module returns one item, so a function with `RETURNS REAL` is correct [B1]. The selection is correct, with the right condition and the right two values returned [B1] [B1]. **The header uses BYREF for Mass. The arrow for Mass points down, so Mass is only passed in and must be by value, and the pseudocode guide does not allow BYREF in a function** [B0]. The answer scores 3 out of 4.

The corrected header is `FUNCTION Surcharge(Mass : REAL) RETURNS REAL`, which is BYVAL by default. The check that catches this slip is to ask of every parameter: does the module need to change it for the caller? A downward arrow only means no.
:::

:::try Start easy, finish at exam standard
Q: Put these in the order of the waterfall life cycle: testing, design, maintenance, analysis, coding.
A: Analysis, design, coding, testing, maintenance.
Q: A structure chart shows an arrow pointing up from module Average to its calling module, labelled Mean. What does the arrow mean?
A: Average passes the value Mean back to the module that called it. It is a returned parameter, so Average could be a function returning Mean.
Q: What does a filled circle at the tail of an arrow mean in a structure chart, and what is the usual data type of the item?
A: It marks a flag, an item of control information such as Valid or Found. A flag is usually a BOOLEAN.
Q: Why is the iterative life cycle better than the waterfall model when the client is unsure what they want?
A: It produces a working version early. The client tries it and their feedback is used in the next cycle, so the requirements can change without redoing signed-off documents.
Q: A state-transition diagram has a double circle. What does it show?
A: A stop (final) state, where the algorithm ends.
Q: What is the name for an arrow in a state-transition diagram that leaves a state and returns to the same state?
A: A loop. The event does not change the state.
Q: A module PrintTotal is given one REAL called Total and returns nothing. Write its header in pseudocode.
A: Nothing comes back, so it is a procedure, and Total is only passed in, so it is by value.

```pseudocode
PROCEDURE PrintTotal(Total : REAL)
```

Q: The module `FUNCTION Discount(Price : REAL, Percent : REAL) RETURNS REAL` is shown in a structure chart. Say how many arrows point down into it and how many point up out of it.
A: Two arrows point down (Price and Percent) and one arrow points up (the returned discount).
Q: In a structure chart, what is shown by a curved arrow across the lines from a module to two modules below it?
A: Iteration: the two modules are called repeatedly, like a loop.
Q: A traffic light has the states Red, Green and Amber, in that order, and a timer event moves it to the next state. List its transitions in a table.
A: Each row is a transition on the event timer.

| Current state | Event | Next state |
|---|---|---|
| Red | timer | Green |
| Green | timer | Amber |
| Amber | timer | Red |
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State the stage of the development life cycle in which each task is carried out: (a) drawing a structure chart; (b) interviewing the staff of a company about what a new program must do; (c) correcting a fault that a user reports six months after release.
A: Each stage earns one mark.

- (a) design [B1]
- (b) analysis [B1]
- (c) maintenance [B1]

Q: [4 marks] ★★ (#cs.development) A hospital in Karachi is developing software to control a machine that delivers medicine into a patient's blood at a set rate. The safety rules for the software are fixed by law. State a suitable life cycle and justify your choice.
H: Is it safe to release a program for this job without full testing? Are the requirements likely to change?
A: Waterfall [B1].

- the requirements are fixed by law, so there is no need to change them during the project [B1]
- a fault could harm a patient, so each stage must be completed, documented and checked before the next [B1]
- thorough testing is planned and carried out after coding, with every stage signed off [B1]

(Accept an iterative life cycle only if the reason shown links to safety checking; RAD is rejected, because prototypes and time boxes do not give the complete verification the scenario needs.)

Q: [3 marks] ★★ A small company in Dubai is developing a website for booking guided city tours. The owner is not sure what the website should look like and wants it online in six weeks. Give two benefits and one drawback of using RAD for this project.
A: Any two benefits and one drawback, each in context.

- a prototype of the booking pages is ready quickly, so the site can go online within six weeks [B1]
- the owner can try each prototype and ask for changes, so the final site matches what they want [B1]
- the owner must be available to review prototypes often, and the time boxes can leave little time for thorough testing and documentation [B1]

Q: [4 marks] ★★ The structure chart in the figure below shows a login program. Write the pseudocode header for each of the three modules ReadEntry, CheckEntry and ShowResult. Entry is a STRING, Attempts is an INTEGER and Correct is a BOOLEAN. CheckEntry should be a function.

:::html
<figure class="fig"><svg viewBox="0 0 520 250" role="img" aria-label="A structure chart. The top module Login calls three modules. ReadEntry passes up Entry as data and Attempts as data. CheckEntry receives Entry and passes up Correct as a flag, drawn with a filled circle. ShowResult receives Correct as a flag and Attempts as data."><text class="tl" x="10" y="26">open circle: data couple</text><text class="tl" x="10" y="44">filled circle: flag</text><rect class="fm s-acc sw2" x="200" y="20" width="120" height="34"/><text class="tl tc" x="260" y="41">Login</text><path class="ln" fill="none" d="M260 54 L260 80"/><path class="ln" fill="none" d="M90 80 L430 80"/><rect class="fm s-acc sw2" x="35" y="170" width="110" height="34"/><text class="tl tc" x="90" y="191">ReadEntry</text><path class="ln" fill="none" d="M90 80 L90 170"/><path class="c1" fill="none" d="M104 120 L104 96" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="104" cy="120" r="3.5"/><text class="tl" x="112" y="112">Entry</text><path class="c1" fill="none" d="M104 154 L104 130" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="104" cy="154" r="3.5"/><text class="tl" x="112" y="146">Attempts</text><rect class="fm s-acc sw2" x="185" y="170" width="150" height="34"/><text class="tl tc" x="260" y="191">CheckEntry</text><path class="ln" fill="none" d="M260 80 L260 170"/><path class="c1" fill="none" d="M246 113 L246 137" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="246" cy="113" r="3.5"/><text class="tl te" x="238" y="129">Entry</text><path class="c1" fill="none" d="M274 137 L274 113" marker-end="url(#ah)"/><circle class="fi" cx="274" cy="137" r="3.5"/><text class="tl" x="282" y="129">Correct</text><rect class="fm s-acc sw2" x="370" y="170" width="120" height="34"/><text class="tl tc" x="430" y="191">ShowResult</text><path class="ln" fill="none" d="M430 80 L430 170"/><path class="c1" fill="none" d="M416 96 L416 120" marker-end="url(#ah)"/><circle class="fi" cx="416" cy="96" r="3.5"/><text class="tl te" x="408" y="112">Correct</text><path class="c1" fill="none" d="M416 130 L416 154" marker-end="url(#ah)"/><circle class="fp s-acc sw2" cx="416" cy="130" r="3.5"/><text class="tl te" x="408" y="146">Attempts</text></svg><figcaption>Structure chart for a login program, used in Exam practice question 4.</figcaption></figure>
:::

A: ReadEntry has two arrows up, so it is a procedure with two BYREF parameters. CheckEntry has one arrow down and a flag up, and is a function returning a BOOLEAN. ShowResult has two arrows down and none up, so it is a procedure with two BYVAL parameters.

```pseudocode
PROCEDURE ReadEntry(BYREF Entry : STRING, BYREF Attempts : INTEGER)
FUNCTION CheckEntry(Entry : STRING) RETURNS BOOLEAN
PROCEDURE ShowResult(Correct : BOOLEAN, Attempts : INTEGER)
```

- ReadEntry: PROCEDURE with Entry and Attempts both BYREF [B1]
- CheckEntry: FUNCTION with parameter Entry as STRING [B1]
- CheckEntry: RETURNS BOOLEAN [B1]
- ShowResult: PROCEDURE with Correct and Attempts passed by value, with the right types [B1]

Q: [4 marks] ★★ A program for a school in Nairobi reads the marks of one pupil in three subjects, finds the mean mark and decides the grade from the mean. The program has the modules ReadMarks, MeanMark, FindGrade and ShowGrade. Copy and complete the table to show what each module is passed and what it passes back. The first row is done for you.

| Module | Passed down into the module | Passed up from the module |
|---|---|---|
| ReadMarks | none | Mark1, Mark2, Mark3 |
| MeanMark | | |
| FindGrade | | |
| ShowGrade | | |

A: Work forward through the data. The three marks come from ReadMarks, MeanMark needs them, FindGrade needs the mean, and ShowGrade needs the grade.

| Module | Passed down into the module | Passed up from the module |
|---|---|---|
| ReadMarks | none | Mark1, Mark2, Mark3 |
| MeanMark | Mark1, Mark2, Mark3 | Mean |
| FindGrade | Mean | Grade |
| ShowGrade | Grade | none |

- MeanMark receives the three marks [B1]
- MeanMark returns the mean [B1]
- FindGrade receives the mean and returns the grade [B1]
- ShowGrade receives the grade and returns nothing [B1]

Q: [5 marks] ★★★ A vending machine in Bogotá sells a snack for two coins. The table is its state-transition table. Its states are Waiting (the start state), HasOne and Sold.

| Current state | Event | Next state | Action |
|---|---|---|---|
| Waiting | coin | HasOne | none |
| HasOne | coin | Sold | give snack |
| HasOne | cancel | Waiting | return coin |
| Sold | take | Waiting | none |

(a) The machine has no row for the event cancel in the state Waiting. State what the machine should do and why the table is incomplete without it. [2 marks]

(b) The events coin, coin, take, coin, cancel happen in that order. State the action taken for each event and the machine's final state. [3 marks]

A: (a) The machine should do nothing and stay in Waiting [B1], because a complete table has a row for every event from every state, including those that change nothing [B1].

(b) Follow the table row by row.

| Event | State after | Action |
|---|---|---|
| coin | HasOne | none |
| coin | Sold | give snack |
| take | Waiting | none |
| coin | HasOne | none |
| cancel | Waiting | return coin |

- first coin: none, and second coin: give snack [B1]
- take: none; third coin: none [B1]
- cancel: return coin and the final state is Waiting [B1]

Q: [6 marks] ★★★ A turnstile at a stadium in Accra has the states Locked (the start state) and Open. The events are token and push. A token in Locked unlocks it and moves it to Open. A push in Open locks it and moves it to Locked. Any other event in either state changes nothing. Write pseudocode that uses a CASE statement on the state to process the events typed by the user. The loop stops when the user types "close".
H: There are two states, each with the events token and push, and the extra event close ends the loop.
A: One possible answer:

```pseudocode
DECLARE State, Event : STRING
State ← "Locked"
INPUT Event
WHILE Event <> "close"
   CASE OF State
      "Locked" :
         IF Event = "token" THEN
            OUTPUT "Unlock"
            State ← "Open"
         ENDIF
      "Open" :
         IF Event = "push" THEN
            OUTPUT "Lock"
            State ← "Locked"
         ENDIF
   ENDCASE
   INPUT Event
ENDWHILE
```

- a variable for the current state set to "Locked" before the loop [B1]
- a loop that reads events and stops when the event is "close" [B1]
- CASE OF State with a case for Locked and a case for Open [B1]
- Locked with token: unlock and the next state is Open [B1]
- Open with push: lock and the next state is Locked [B1]
- all other events leave the state unchanged (no ELSE branch changes State) [B1]

Q: [4 marks] ★★★ A firm that writes software for a bank must produce a program that follows new regulations published in full six months before they take effect. Compare the use of the waterfall model with the iterative model for this project and recommend one.
H: Are the requirements fixed? What does each model do well in that case?
A: A recommendation with reasons from the scenario.

- the regulations are published in full and will not change, so the requirements are fixed and known in advance [B1]
- waterfall plans everything and documents each stage, which suits fixed requirements and gives a clear date for completion [B1]
- iterative would give a working version sooner but its main advantage, handling changing requirements, is not needed [B1]
- recommend waterfall (or iterative with a justification that links to the fixed deadline) [B1]
:::

:::try Stretch for A*
Q: A structure chart is given as an outline. The top module ManageStock repeats (iteration) these steps until the user quits: GetAction (passes up Action, a CHAR), then a selection between SellItem (passed Code, a STRING, returns Price, a REAL) and RestockItem (passed Code and Amount, an INTEGER, returns nothing). GetAction also passes up Code and the flag Quit. Write the pseudocode header of each module and a main program for ManageStock that repeats until Quit is TRUE and uses Action to choose between SellItem ('S') and RestockItem ('R').
H: Which module sends the flag, and which parameters are BYREF?
H: A selection in a structure chart is an IF or CASE in the calling module, and an iteration is its loop.
A: GetAction returns three items, so it is a procedure with three BYREF parameters. SellItem returns one item, so it is a function. RestockItem returns nothing, so it is a procedure with BYVAL parameters.

```pseudocode
PROCEDURE GetAction(BYREF Action : CHAR, BYREF Code : STRING, BYREF Quit : BOOLEAN)
FUNCTION SellItem(Code : STRING) RETURNS REAL
PROCEDURE RestockItem(Code : STRING, Amount : INTEGER)
```

The main program:

```pseudocode
DECLARE Action : CHAR
DECLARE Code : STRING
DECLARE Quit : BOOLEAN
DECLARE Price : REAL
DECLARE Amount : INTEGER

Quit ← FALSE
WHILE Quit = FALSE
   CALL GetAction(Action, Code, Quit)
   IF Quit = FALSE THEN
      CASE OF Action
         'S' : Price ← SellItem(Code)
               OUTPUT "Price: ", Price
         'R' : OUTPUT "Amount to add"
               INPUT Amount
               CALL RestockItem(Code, Amount)
      ENDCASE
   ENDIF
ENDWHILE
```

The WHILE loop is the iteration symbol, and the CASE is the selection diamond. The flag Quit is tested before an action is carried out, so quitting does not run SellItem or RestockItem by mistake.

Q: A parity checker reads a string of the characters '0' and '1' and decides whether the string contains an even number of 1s. Draw its state-transition diagram in words, with two states, and write pseudocode that uses a CASE on the state for the string "10110" (given in the array Bits[1:5] of CHAR). What does the program output?
H: Pressing a 0 never changes the state. What does a 1 do?
A: The states are Even (the start state, and the accepting state) and Odd. The event '0' is a loop in both states. The event '1' moves Even to Odd and Odd to Even.

```pseudocode
DECLARE Bits : ARRAY[1:5] OF CHAR
DECLARE State : STRING
DECLARE Index : INTEGER

State ← "Even"
FOR Index ← 1 TO 5
   IF Bits[Index] = '1' THEN
      CASE OF State
         "Even" : State ← "Odd"
         "Odd" : State ← "Even"
      ENDCASE
   ENDIF
NEXT Index
OUTPUT State
```

The string 10110 has three 1s: Even → Odd (1) → Odd (0) → Even (1) → Odd (1) → Odd (0), so the program outputs Odd. An odd count means the string is not accepted. The diagram has no stop state because the string ends when the characters run out.
:::

:::quiz
? Which stage of the development life cycle produces the structure chart and the test plan?
- analysis
+ design
- coding
- maintenance
> Analysis defines the problem; design plans the solution, including structure charts, algorithms and the test plan. Coding then writes the program from those plans.
? In the waterfall model, what is the main drawback when a client changes their mind halfway through?
- The program cannot be tested.
- Programmers must start coding before the design is complete.
+ Earlier documents must be redone and signed off again, which is costly.
- The client cannot change anything after the first stage, even at the end.
> Because each stage is completed and signed off in order, a change to the requirements means going back and reworking earlier stages. The other options are not features of the waterfall model.
? A company wants to release a first version of an app within a month and then add features according to what users ask for. Which life cycle fits best?
- waterfall
+ iterative or rapid application development
- no life cycle is needed
- waterfall, because it gives the most documentation
> The requirements are expected to change and the client wants a working version early, which iterative and RAD cycles provide. Waterfall delivers its first working version late.
? Which statement about RAD is correct?
- It has no design stage.
- It does not need users to take part.
+ It builds prototypes in short time boxes and uses feedback from users.
- It is best for safety-critical systems.
> RAD still designs and tests, but in short cycles, with users reviewing each prototype. Its weakness is that it is less suited to safety-critical systems, which need complete planning.
? In a structure chart, what does an arrow pointing up from a module to the module above it show?
- The module above runs after this module.
- The modules are called repeatedly.
+ Data passed back from the lower module to the module that called it.
- The module is a function.
> Arrows show the direction data travels, up or down, not the order of execution. A returned value may come from a function but may also be a BYREF parameter of a procedure.
? A module is passed Price and Rate and returns a Total. Which header matches it?
- `PROCEDURE Cost(BYREF Price : REAL, BYREF Rate : REAL) RETURNS REAL`
- `FUNCTION Cost(BYREF Price : REAL, BYREF Rate : REAL) RETURNS REAL`
+ `FUNCTION Cost(Price : REAL, Rate : REAL) RETURNS REAL`
- `PROCEDURE Cost(Price : REAL, Rate : REAL)`
> It returns one value, so it is a function, and the two items only come in, so they are by value. A procedure cannot have RETURNS, and a function cannot use BYREF.
? In a state-transition diagram, what does an arrow labelled `coin / unlock` mean?
- When the system unlocks, a coin is inserted.
+ When the event coin happens, the system performs the action unlock and moves to the state at the arrow's head.
- The coin is the next state.
- The system waits for the unlock button.
> The label is event / action. The event causes the transition, the action is what the system does, and the arrow's head is the next state.
? A state-transition diagram for a lift shows a state with no arrow for the event "door blocked". What is the problem?
- No problem: unlisted events are ignored by every system.
+ The diagram is incomplete, because every event in the scenario needs an arrow from every state, even if the state does not change.
- The lift will stop working.
- The diagram must be drawn as a structure chart instead.
> A state-transition diagram documents the full behaviour. If an event does nothing in a state, a loop labelled with that event (or a row in the table) says so.
:::

:::checklist What you can now do
- [ ] I can explain the purpose of a program development life cycle and the need for different life cycles for different programs.
- [ ] I can describe the analysis, design, coding, testing and maintenance stages and what each produces.
- [ ] I can describe the principles, benefits and drawbacks of the waterfall, iterative and RAD life cycles.
- [ ] I can choose a life cycle for a scenario and justify the choice.
- [ ] I can explain the purpose of a structure chart.
- [ ] I can read a structure chart, including data couples, flags, selection and iteration.
- [ ] I can construct a structure chart for a problem and show the parameters passed between modules.
- [ ] I can derive pseudocode headers and calls from a structure chart.
- [ ] I can explain the purpose of a state-transition diagram and draw one with states, events and actions.
- [ ] I can turn a state-transition diagram or table into pseudocode with CASE.
:::

:::recap
- The life cycle has five stages: analysis (requirements), design (structure chart, algorithms, test plan), coding, testing, maintenance. It gives structure, quality and a record for later changes.
- Waterfall: strict order, sign-off at each stage, thorough documents, late working program, costly change. Suits fixed requirements and safety-critical projects.
- Iterative: repeated laps of design, code and test, each giving a working version and feedback. Handles change but the cost and end date are uncertain.
- RAD: fast prototypes, users involved all the time, time boxes, reused components. Quick and flexible, but needs the users, can be poorly documented and is not for safety-critical systems.
- A structure chart shows modules in a hierarchy. A down arrow is data passed in, an up arrow is data returned. Open circle = data couple, filled circle = flag, curved arrow = iteration, diamond = selection. Arrows show data, not order.
- From a chart: a module returning one item is a function (never BYREF); a module returning none or several is a procedure with BYREF for the items passed back.
- A state-transition diagram has states (circles), transitions (arrows labelled event / action), a start arrow, loops and double circles for stop states. It needs every event from every state. In code it is a CASE on the state inside a loop.
:::

:::links
- practise: [Program development life cycle: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/12-software-development-/program-development-life-cycle/exam-questions/) · Save My Exams · 9618-style questions on life cycles with mark schemes [paid]
- practise: [Program design: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/12-software-development-/program-design-/exam-questions/) · Save My Exams · structure chart and state-transition questions [paid]
- read: [Ada Computer Science](https://adacomputerscience.org/) · Ada Computer Science · free explanations of the software development life cycle and program design
- explore: [Python Tutor](https://pythontutor.com/visualize.html) · Python Tutor · paste the parcel program and watch each module run in turn
- read: [The 9618 syllabus](https://www.cambridgeinternational.org/Images/721397-2027-2029-syllabus.pdf) · Cambridge · section 12 lists what you must know

Links checked 13 November 2026.
:::

Next: [Testing, errors and maintenance](#cs.testing)
