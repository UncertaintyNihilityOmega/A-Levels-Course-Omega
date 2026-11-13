@chapter cs.ethics
@title Ethics, ownership and the impact of AI
@level as
@paper CAIE 9618 Paper 1
@time 3–4 hours
@summary Why computing professionals need a code of ethics and what bodies such as BCS and IEEE do, how to judge whether an action in a scenario is ethical, why copyright law exists, how free software, open source, shareware and commercial licences differ and which to choose, and the social, economic and environmental impact of artificial intelligence.

:::why
Software now decides who gets a loan, what news you see and whether a medical scan is flagged. The people who write it make choices that affect millions of people who will never meet them. This topic asks you to reason about those choices in a scenario: what is right, who owns the work, which licence fits, and what a technology such as AI changes for people, jobs and the planet. The marks go to a clear point, a reason and, for scenarios, a link to the details you were given.
:::

**Before you start**, you should know what data privacy is, and what hackers and malware do, from [Security, privacy and data integrity](#cs.security).

:::try Warm-up
Q: Explain the difference between data security and data privacy. (from [Security, privacy and data integrity](#cs.security))
A: Security is protecting data from unauthorised access, damage or loss. Privacy is a person's right to control how their personal information is collected, used and shared.
Q: What is a hacker, and how does that differ from a person who is paid to test a system's defences? (from [Security, privacy and data integrity](#cs.security))
A: A hacker gains access to a system or data without permission. A person paid to test the defences has the owner's permission and reports the weaknesses so that they can be fixed.
Q: State one way a company could lose customers' trust after a security breach. (from [Security, privacy and data integrity](#cs.security))
A: Customers' personal data is stolen and made public, so they no longer trust the company with their details and may take their business elsewhere.
:::

## Ethics for computing professionals

:::def Ethics
The moral principles that guide how people decide what is right and wrong. In computing, ethics is about how computer systems should be designed, built, used and shared so that they are fair and do not harm people.
:::

Anyone can act ethically or unethically, but a **computing professional** carries extra responsibility, for four reasons:

- Their work reaches **many people**: one program can be used by millions, so one mistake or one unfair rule is repeated at huge scale.
- The public **cannot easily check** it. Most people cannot read code or know what is done with their data, so they must trust the people who wrote the system.
- Computers hold **power and information**: personal records, money, medical details, and sometimes people's safety (a medical device, an aircraft).
- Laws change slowly and technology changes fast, so there are many situations where **no law says what to do**, and the professional has to decide.

### Ethics and the law

Law and ethics are related but not the same. A law is a rule made by a government and enforced by courts. Ethics is about what is right, whether or not a law says so.

:::key Ethics is not the same as the law
- An action can be **legal but unethical**: a company may be allowed to sell the browsing history of its users in small print, yet users never expected it and would object.
- An action can be **ethical but not required by law**: a developer tells a client about a weakness in a system, although no law forces the developer to.
- Laws differ from country to country, so an action can be legal in one place and an offence in another. An ethical professional asks "is this right?" as well as "is this allowed?".
:::

### What a professional should do

Professional codes differ in wording, but they share the same ideas. You should be able to use them to judge a scenario.

:::key Ethical principles for a computing professional
- **Act in the public interest**: think about the safety, health, privacy and wellbeing of the people the system affects, and of the environment.
- **Be competent**: accept only work you are able to do, keep your skills up to date, and do not claim skills you do not have.
- **Be honest**: do not mislead clients, employers or users; report faults and risks truthfully, and admit mistakes.
- **Respect confidentiality and privacy**: use personal data only for the purpose it was given for, and keep it safe.
- **Respect ownership**: do not copy other people's work, or use it against its licence.
- **Treat people fairly**: do not discriminate, and do not build systems that treat groups of people unfairly.
- **Meet your duties** to your employer or client, and to the profession, without breaking the duty to the public.
:::

### Professional ethical bodies

:::def Professional ethical body
An organisation that people working in a profession can join, which sets standards of professional conduct (a code of conduct or ethics) that its members agree to follow, and which supports its members and the profession.
:::

Two bodies are named in the syllabus.

| | BCS | IEEE |
|---|---|---|
| What it is | The Chartered Institute for IT, the professional body for information technology in the United Kingdom | A large international professional organisation for engineers and technologists, including computer scientists |
| Its code | A Code of Conduct, organised under four headings: public interest, professional competence and integrity, duty to the relevant authority (such as an employer or client) and duty to the profession | A Code of Ethics: its themes include putting the safety, health and welfare of the public first, honesty, avoiding conflicts of interest and treating all people fairly |

Bodies like these do four main jobs:

- They set a **code of conduct** that members promise to follow, and can take action against a member who breaks it.
- They set and promote **professional standards**, including recognised qualifications and levels of membership that show an employer a person's skill and commitment.
- They support **professional development**: training, conferences, journals and ways of keeping up to date, so members stay competent.
- They give the profession a **voice**: they advise governments and the public, and give members somewhere to go for advice.

Why should a professional join? A code gives you a clear standard to point to if you are asked to do something wrong ("my professional code does not allow me to"); membership shows employers and the public that you can be trusted; and the body helps you to stay up to date. The public gains too: they can trust that a member works to agreed standards, and know where to complain.

### Judging a scenario

Questions give a short scenario and ask whether an action was ethical, and what its impact is. Use the principles as a checklist, and always link your answer to the details you are given.

:::steps
1. Identify the **action** (what exactly was done or asked).
2. Ask **who is affected** and how: users, the public, the employer, the profession.
3. Match it to a **principle**: honest? in the public interest? confidential? respecting ownership? fair?
4. State the **impact**: harm to people, loss of trust, legal trouble for the company or the person, damage to the profession's reputation.
:::

:::eg Explaining unethical actions (exam style)
A developer at a company in Nairobi writes a phone app that records where its users go. The manager tells the developer to (a) send each user's location to an advertising company without telling the users, and (b) release the app even though testing found a fault that lets some users see other users' locations. Explain **two** actions that are unethical, and the impact of each. [6 marks]

Take each action in turn: name it, say which principle it breaks, and give an impact.

- Sending the users' locations to an advertiser without telling them is unethical [B1] because it breaks their privacy and confidentiality: the data is used for a purpose they have not agreed to [B1]. The impact is that users lose trust in the app and the company, and the company may break data protection laws [B1].
- Releasing the app with a known fault is unethical [B1] because the fault is a risk to the public: strangers could see where a user is, which could put them in danger [B1]. The impact is possible harm to users, loss of reputation for the company, and legal action [B1].

A strong answer also shows what an ethical developer would do: refuse, report the problem and the risk to the manager (and if necessary a higher authority), and leave the release until the fault is fixed.
:::

:::eg Explaining an ethical action
A tester at a software company in Karachi finds that a program that controls the dose given by a hospital machine can show a wrong value on screen when a rare combination of settings is used. The deadline is tomorrow. Explain what the tester should do and why. [3 marks]

- The tester should report the fault, with the details of how to repeat it, to the project manager at once, even though the deadline will be missed [B1], because patients' safety (the public interest) matters more than the deadline [B1].
- The tester should not sign off the software as tested or hide the fault, because that would be dishonest and would put patients at risk [B1].
:::

:::warn Do not just write "it is wrong"
"It is unethical" earns no mark on its own. Say which principle is broken (privacy, honesty, public safety, ownership, fairness) and use the details in the scenario. An answer that only lists "it is illegal" misses the point if the question asks about ethics.
:::

## Copyright and software ownership

When someone writes a program or a song, or draws a picture, copying it takes seconds and costs almost nothing. Without protection, the creator would earn nothing from their work. **Copyright** law exists to give the creator control.

:::def Copyright
A legal right that gives the creator of an original work, such as a program, a piece of music or a book, the right to decide who may copy, distribute, change or perform it, for a limited period. In most countries it applies automatically when the work is created.
:::

Computer programs are protected as original works: the source code, and the text, images and sounds that come with a program. Copyright protects the **way a program is written**, not a general idea. Writing your own program that does the same job as another is not an offence; copying their code is.

:::key Why copyright legislation is needed
- It lets creators **earn from their work** (people buy a licence instead of copying), which encourages them to keep creating.
- It **stops others from copying and selling** the work, or claiming it as their own.
- It gives owners a **legal remedy** (they can take a court action, or demand payment) when their work is copied.
- It supports **innovation**: companies invest in developing software because they can protect their investment.
:::

:::def Software piracy
The illegal copying, sharing or use of software without the permission of the copyright owner.
:::

Examples of piracy include making copies of a bought program for friends, installing a single-user program on many computers, running software with a licence-breaking "cracked" code, and selling copies. A person or company that does this risks fines or court action, the software may carry malware, and the developer loses the income that pays for support and new versions. Copying code from a website or a colleague and putting it into your own work is also a breach of copyright, unless the licence allows it.

## Software licences

Bought software is not usually "owned" by the user. The user buys a **licence**, a permission to use the program under conditions.

:::def Software licence
A legal agreement between the owner of software and its user that states how the software may be used, copied, changed and shared.
:::

You must know four kinds.

### Free software

:::def Free software
Software that gives its users four freedoms, as the Free Software Foundation (FSF) defines them: to run the program for any purpose; to study how it works and change it (which needs the source code); to redistribute copies; and to distribute copies of the changed versions.
:::

"Free" here means **freedom, not price**. A free software program may be sold; what matters is the freedom of the user. Many free software licences are **copyleft**: anyone who distributes a changed version must give the users of that version the same freedoms. The GNU General Public License is a well-known example.

### Open source software

:::def Open source software
Software whose source code is available for anyone to read, and which is released under a licence that meets the Open Source Definition of the Open Source Initiative (OSI). The licence allows the software to be redistributed and changed.
:::

The OSI's definition has ten conditions, including free redistribution, access to the source code, permission to make derived works, and no discrimination against any person or group or any field of use. Most free software is also open source, and the other way round, but the two groups stress different things: the Free Software Foundation stresses the **freedom** of the user, the Open Source Initiative stresses the **practical benefits** of sharing code. Open source licences differ in their conditions: some are copyleft (changes must be shared under the same licence), and others allow the code to be used in programs whose source code is kept secret. Always say "open source is **not always free of conditions**".

### Shareware and commercial software

:::def Shareware
Software that users can try for free, usually for a limited time or with some features missing, and must pay for if they want to carry on using it or to unlock the full version. The author keeps the copyright and the source code is not supplied.
:::

:::def Commercial software
Software that is sold to users (once, or by regular subscription) under a licence that sets out how many copies or users are allowed. The source code is not supplied, and users may not copy, change or share the program.
:::

:::key Comparing the four licences
| | Free software (FSF) | Open source (OSI) | Shareware | Commercial |
|---|---|---|---|---|
| Source code | available | available | not available | not available |
| May the user change it? | yes | yes (licence conditions apply) | no | no |
| May the user share copies? | yes | yes (licence conditions apply) | only in its trial form | no |
| Cost | may be free of charge or sold | often free of charge | free trial, then pay | pay for a licence |
| Support | community or paid support | community or paid support | from the author | normally from the supplier |
:::

:::warn Free software, freeware and open source are three different things
**Free software** means freedom for the user, not "no cost". **Freeware** costs nothing, but you cannot see or change the source code, so it is not free software. **Open source** means the source code is available and the licence meets the OSI's definition, but the licence may still have conditions.
:::

### Choosing a licence

To **justify** a licence, give reasons that come from the scenario. Use these questions:

- Is there money to buy it, or is cost the main concern (a free or open source licence)?
- Does the user need to **change** the program (open source or free software, because the source is available)?
- Does the user need guaranteed **support**, updates and someone to hold responsible (commercial)?
- Does the **developer** want to earn money (commercial or shareware), or to share the work and let others improve it (open source)?
- Does the developer need to keep the source code **secret** (commercial or shareware)?

:::eg Justifying a licence (exam style)
A school in Accra has 120 computers and a small budget. It wants a word processor that its teachers can change, so that the menus appear in the local language. A commercial licence costs 15 dollars per computer per year. Justify the licence the school should choose. [4 marks]

The commercial licence would cost \(120 \times 15 = 1800\) dollars each year, or 5400 dollars over three years. [B1]

The school should choose an open source (or free software) word processor. There is no licence fee, so the 1800 dollars a year could be spent on other things [B1]. The source code is available, so a teacher or a local programmer can change the program to show the menus in the local language, which a commercial licence does not allow [B1]. The licence lets the school install the program on all 120 computers without paying for each [B1].

A fair answer also notes a drawback: support usually comes from a community rather than a company, so the school needs someone who can help staff to use and look after it.
:::

:::eg Choosing between commercial and open source
A small software company in Manila has written an accounting program. It wants to earn money from it and does not want competitors to copy the code. State a suitable type of licence and justify it. [3 marks]

- A commercial licence (customers pay for a licence to use it). [B1]
- Customers pay for each licence (or subscription), so the company earns the money it needs to pay for developing and supporting the program. [B1]
- The source code is not supplied and users may not copy or change the program, so competitors cannot copy the code. [B1]
:::

## Artificial intelligence: applications and impact

:::def Artificial intelligence (AI)
The ability of a computer system to do tasks that would normally need human intelligence, such as understanding language, recognising images, making decisions and learning from data.
:::

AI is no longer a laboratory idea. Everyday applications include:

- **Medical diagnosis**: a system studies scans or test results and flags signs of disease for a doctor to check.
- **Autonomous vehicles**: a car or bus uses cameras and sensors to read the road and drive.
- **Fraud detection**: a bank's system learns what a customer's normal payments look like and flags unusual ones.
- **Language translation and speech recognition**: text and speech are converted between languages, and spoken words become text.
- **Recommendation systems**: a shop or video service suggests what to buy or watch, based on what similar users chose.

How these systems learn is an A Level topic (see [Machine learning and neural networks](#cs.ml)). For the AS course, you need to be able to say what they do and how they affect people.

### Social, economic and environmental impact

Examiners ask about the impact of a given AI system. Organise your answer in three groups, and give a benefit **and** a concern where you can.

:::cols
:::col Social impact
**Benefits**: faster and more accurate diagnosis and so better healthcare; services that are available to more people (translation, captions for people who are deaf); fewer accidents if a vehicle is driven more carefully than a tired person.

**Concerns**: **bias**, where a system trained on unfair or incomplete data treats some groups of people unfairly; **privacy**, because AI needs large amounts of personal data, which can be misused or used for surveillance; **accountability**, because it can be hard to say who is responsible when an AI makes a harmful mistake; loss of human contact; people trusting a system too much.
:::
:::col Economic impact
**Benefits**: tasks done faster and at lower cost, so businesses are more productive; new industries and new kinds of job (for example people who build and check AI systems); products become cheaper or better.

**Concerns**: some jobs are done by machines, so some workers lose work and need retraining; the gains may go mainly to the companies that own the systems, increasing inequality; developing AI costs a lot, which may favour large organisations and rich countries.
:::
:::

:::cols
:::col Environmental impact
**Benefits**: AI can reduce waste and energy use, for example by controlling the heating of a large building or the supply and demand on an electricity grid, improving traffic flow, or analysing satellite images to monitor forests and weather.

**Concerns**: training large AI systems and running them in data centres uses a lot of electricity, and the cooling of the equipment can use a lot of water; making and replacing the computers needed causes electronic waste.
:::
:::col How to write a good answer
1. Say what the system **does** in the scenario.
2. Give impacts under the headings your question asks for.
3. For each, name the **group affected** (patients, drivers, workers, the company) and say what changes.
4. Give both sides if the question says "discuss", and a short judgement at the end.
:::
:::

:::eg Impact of an AI system (exam style)
A city plans to use self-driving buses that use AI to read the road. Discuss the impact of this system. Refer to the social, economic and environmental impact in your answer. [6 marks]

- Social: the buses may be safer, because the system does not get tired or distracted, so fewer accidents [B1]. However, if the AI misreads a situation and crashes, it may be unclear who is responsible, and people may not trust the system [B1].
- Economic: the city would not pay drivers' wages, so the service may be cheaper to run [B1]. However, bus drivers could lose their jobs and need to retrain, and the buses are expensive to buy and maintain [B1].
- Environmental: the vehicles can be driven smoothly, which saves fuel or electricity, and the system can plan routes to reduce the number of empty journeys [B1]. However, building the vehicles and running the computers that power the AI uses energy and resources [B1].

Two marks are given for each of the three headings, one for a clear benefit and one for a concern or a link to the scenario. An answer that gives only benefits can score at most half of the marks.
:::

:::eg Spot the error: licences
Question: Explain the difference between free software and shareware. [4 marks]

A student wrote:

```text
01  Free software is software that costs nothing, so the company that wrote it
02  cannot sell it. Shareware is software that you can try before you buy: it
03  is free for a trial period and you have to pay to carry on using it.
04  With shareware the source code is not available, but with free software
05  the source code is available so that users can change it.
```

Line 01 is wrong: in free software, "free" means freedom (to run, study and change, and share it), not "costs nothing", and the software may be sold [B0]. Lines 02 and 03 describe shareware correctly: a free trial, then payment to keep using it [B1] [B1]. Lines 04 and 05 state a correct difference: source code available with free software and not with shareware [B1]. The answer scores 3 out of 4.

The fix for line 01: "Free software gives users the freedom to run, study, change and share it; 'free' refers to freedom, not price."
:::

:::try Start easy, finish at exam standard
Q: State what is meant by ethics in computing.
A: The moral principles that guide how computer systems should be designed, built and used so that they are fair and do not harm people.
Q: Name two professional bodies for computing professionals.
A: BCS (the Chartered Institute for IT) and IEEE.
Q: Give two things that a professional ethical body does.
A: Any two: sets a code of conduct that members follow; sets professional standards and qualifications; supports members' professional development; gives the profession a voice to advise governments and the public.
Q: Give one reason why an action can be legal but still unethical.
A: Laws do not cover everything and differ between countries, so a company may be allowed to do something, such as sell users' data hidden in small print, that users would object to and that harms them.
Q: A programmer copies a program that a friend bought and installs it on four other computers. Which law has been broken, and what is this called?
A: Copyright law has been broken. The copying and use without permission is software piracy.
Q: State why copyright legislation is needed.
A: It protects the creators' rights, so that others cannot copy their work and sell it, which lets creators earn from their work and encourages them to continue.
Q: Does the phrase "free software" mean that the software costs nothing?
A: No. "Free" means freedom to run, study, change and share the software, not that it costs nothing. Free software may be sold.
Q: Which of free software, open source, shareware and commercial software is supplied without its source code and is free to try, but must be paid for to continue using?
A: Shareware.
Q: Give one social concern about the use of AI.
A: Bias: a system trained on unfair or incomplete data may treat some groups of people unfairly. (Also accepted: loss of privacy, unclear responsibility for mistakes, loss of jobs.)
Q: Give one environmental benefit and one environmental concern of AI.
A: Benefit: it can reduce energy waste, for example by controlling building heating or traffic flow. Concern: training large systems and running data centres uses a lot of electricity (and water for cooling).
:::

:::try Exam practice ★ to ★★★
Q: [3 marks] ★ State three things that a professional ethical body such as BCS or IEEE does.
A: Any three of:

- sets a code of conduct (or ethics) for its members to follow [B1]
- sets and promotes professional standards, such as qualifications and levels of membership [B1]
- supports members' professional development, such as training and keeping their skills up to date [B1]

(Also accepted for any one of the three: gives a voice to the profession, advising governments and the public; can take action against a member who breaks the code. Only three marks can be awarded.)

Q: [4 marks] ★ (a) Explain why copyright legislation is needed for software. [2] (b) Give two examples of software piracy. [2]
A: (a) It stops other people from copying the software and selling it or claiming it as their own [B1], so that the people who write software can earn money from their work and continue to develop it [B1].

(b) Any two examples: making copies of a program and giving them to other people; installing a single-licence program on more computers than the licence allows; selling copies of the program; using software with an illegal licence code [B1] [B1].

Q: [6 marks] ★★ A programmer at a company in Cape Town writes a health-tracking app. The manager tells her to (a) release the app although testing has found a fault that sometimes shows one user's health data to another user, and (b) copy a block of code from an online forum into the app without checking its licence, which says that it may not be used in a commercial product. Explain **two** actions that are unethical. For each, state why it is unethical and the impact. [6]
H: Take one action at a time: name it, say which principle it breaks, and then say who is harmed and how.
A: Action (a), releasing the app with a known fault, is unethical [B1] because it risks the privacy of users and does not put the public interest first, since the users' private health data could be seen by strangers [B1]. The impact is harm to users and a loss of trust in the company, and the company may be in trouble under data protection law [B1].

Action (b), using the copied code, is unethical [B1] because it breaks the code's licence and the copyright of its author, so it does not respect ownership [B1]. The impact is that the company could be taken to court, may have to pay or to remove the code, and the programmer's reputation would suffer [B1].

Q: [6 marks] ★★ (#cs.ethics) A teacher in Accra wants a program for the school computers. The school has little money, and the teacher wants the program to be adapted to the local language. (a) State what is meant by shareware. [2] (b) Justify why an open source licence would suit the school better than shareware. [3] (c) State one drawback of open source software for the school. [1]
A: (a) Software that is free to try for a limited time, or with limited features [B1], and which the user has to pay for to carry on using it or to unlock the full version [B1].

(b) Open source software usually has no licence fee, which suits the school's small budget [B1]. The source code is available, so it can be changed to support the local language, while shareware does not allow users to change the program [B1]. Shareware needs a payment at the end of the trial, but the open source program can be used for as long as the school likes [B1].

(c) Support is normally given by a community and not guaranteed by a company, so staff may find it harder to get help. (Accept: some licences require changes to be shared.) [B1]

Q: [6 marks] ★★ A hospital in Lagos uses an AI system to look at X-ray images and to mark those that may show a broken bone, for a doctor to check. Describe one social, one economic and one environmental impact of the system. [6]
H: For each, give a statement and then a reason or a consequence in the hospital.
A: Social: patients may be diagnosed faster and more accurately [B1], because the system can check many images quickly and a doctor then has more time for patients (or, as a concern: the system may be less accurate for groups that were missing from its training data, which would be unfair) [B1].

Economic: the hospital can deal with more patients with the same staff, which reduces costs [B1], though it has to pay to buy and maintain the system, and the jobs of some staff who look at images may change [B1].

Environmental: the system needs powerful computers that use electricity (and cooling) [B1], but faster diagnosis may mean fewer repeat scans and visits, reducing the energy and travel of patients (or the concern: the equipment will eventually become electronic waste) [B1].

Q: [8 marks] ★★★ A bank uses an AI system to decide whether to approve loans, using customers' past records. Discuss the impact of this system. Refer to the social, economic and environmental impact in your answer. [8]
H: Aim for three points on social impact, three on economic impact and two on environmental impact, with a benefit and a concern among them.
A: Any points of this kind, up to 8 marks, with at most 3 for social, 3 for economic and 2 for environmental.

Social:

- decisions are made quickly and in the same way for every applicant, which may be fairer than a tired or prejudiced person [B1]
- the system may learn bias from past records, for example refusing loans to groups that were refused in the past [B1]
- applicants' private financial data is collected and could be misused or leaked, and it can be hard to explain or challenge a decision (accountability) [B1]

Economic:

- the bank saves money, because fewer staff are needed to assess each loan, and can serve more customers [B1]
- some staff who assess loans may lose their jobs or need to change roles [B1]
- wrong decisions may cost the bank money (bad loans) or cost customers a chance to start a business [B1]

Environmental:

- processing a large number of applications uses electricity in the bank's data centres [B1]
- loans are decided online, so customers do not need to travel to a branch, which saves journeys [B1]

Q: [6 marks] ★★ (#cs.ethics) A company in Warsaw is allowed by law to sell the email addresses of its customers to other companies, because a clause in its long terms and conditions says that it can. (a) Explain why this could still be unethical. [3] (b) State how an ethical computing professional working at the company should respond when asked to prepare the list. [3]
A: (a) The law allows it, but being legal does not make an action ethical [B1]. Customers did not expect their data to be shared and probably did not read the clause, so their privacy is not respected [B1], and they may lose trust in the company or receive unwanted messages [B1].

(b) Question the request and explain the concern to the manager [B1]; suggest asking customers for clear, separate permission (a request that is easy to understand) [B1]; if the company still insists, refuse to take part and, if necessary, report it, using the professional code as support [B1].
:::

:::try Stretch for A*
Q: [5 marks] ★★★ A company uses an AI system to help decide which job applicants to interview. The system was trained on the company's records of the people it hired over the last twenty years. Most of the people hired in that time were men. Explain how the system may treat women unfairly, and describe two ways in which the company could reduce the problem.
H: Think about what the system learns from the training data.
H: One way concerns the data it is trained on; the other concerns checking what it does.
A: The training data records past decisions, which contain the bias of the people who made them [B1]. The system learns the pattern that men were hired more often and may repeat or increase it, so it scores women lower for the same skills [B1]. That is discrimination against women, and the company may not notice, because the system seems objective [B1].

Ways to reduce the problem (any two of these):

- train the system on balanced data that is representative of all applicants, or remove features that reveal gender [B1]
- regularly test the system's results for unfair differences between groups of applicants [B1]
- (an accepted third way, with the same mark: have a person review the decisions, especially when someone is rejected)

Q: [5 marks] ★★★ A developer releases a code library under a copyleft free software licence. A company wants to use it in a new commercial program. (a) State one freedom that the licence gives the company. [1] (b) Explain what the copyleft condition would mean for the company if it distributes its program to customers. [2] (c) Explain why the company might still prefer to write its own library instead. [2]
H: Copyleft means that anyone who distributes a changed or combined version must pass on the same freedoms.
A: (a) Any one of: to run the library for any purpose; to study and change it; to redistribute copies; to distribute its changed versions [B1].

(b) The company must give its customers the same freedoms, including access to the source code, for the program that includes the library [B1], so it could not keep its own code secret or sell copies on the condition that customers may not share them [B1].

(c) The company wants to keep its source code secret and to control how customers use the program [B1], and a library it writes itself has no copyleft conditions, so it can use a commercial licence [B1].
:::

:::quiz
? What does a professional ethical body such as BCS or IEEE do?
- It writes the laws that apply to computing.
+ It sets a code of conduct for its members and supports their professional development.
- It makes sure that all software is free.
- It tests every program before it is sold.
> A professional body sets and promotes standards for its members. Laws are made by governments, and testing software is the job of the developers.
? An action is legal, but it harms people and is done without telling them. What can you say about the action?
- It must be ethical, because it is legal.
+ It may still be unethical, because ethics is about what is right as well as what is allowed.
- It must be illegal in another country.
- It is ethical if the company earns money.
> Law and ethics are different. Many actions that are not forbidden by law still harm or mislead people.
? Which is the best reason for copyright legislation?
- It makes all software free to copy.
+ It lets creators control copying, so they can earn from their work and are encouraged to create more.
- It prevents anyone from writing similar programs.
- It stops programs from containing faults.
> Copyright protects a particular work from being copied without permission. It does not stop others writing their own program.
? What does the "free" in free software mean?
- The software costs nothing.
- The software has no licence.
+ Users are free to run, study, change and share it.
- The software has no faults.
> The Free Software Foundation defines free software by four freedoms. It can be sold, and it always has a licence that grants those freedoms.
? A program is free to try for 30 days, and the user must then pay to carry on using it. Which licence is this?
- Open source
- Free software
+ Shareware
- Copyleft
> This is shareware: a free trial, then payment. Free and open source software are not defined by a time limit.
? A developer wants other people to read, change and improve a program, and does not want to charge for it. Which licence suits this best?
- Commercial
- Shareware
+ Open source
- None, because the program belongs to the world.
> Open source licences make the source code available and allow it to be changed and shared. Commercial and shareware licences do not supply the source code, and the program still has an owner under copyright.
? A facial-recognition system works well for some groups of people and poorly for others. What is the most likely cause?
- The cameras are too expensive.
+ The data it was trained on did not represent all groups equally.
- AI systems always make random errors.
- The program was not compiled.
> Bias often comes from training data that is incomplete or unfair. The system learns patterns from that data and repeats them.
? Which is an environmental concern about AI?
- AI makes some jobs unnecessary.
- AI can be used to spy on people.
+ Training and running large AI systems in data centres uses a lot of electricity.
- AI can make a decision that is hard to explain.
> Job loss is an economic concern, and surveillance and accountability are social concerns. Electricity and cooling for data centres are environmental concerns.
:::

:::checklist What you can now do
- [ ] I can explain the need for ethics for computing professionals, and why ethics is not the same as the law.
- [ ] I can describe what professional bodies such as BCS and IEEE do, and why a professional should join one.
- [ ] I can say whether an action in a scenario is ethical or unethical, and explain its impact using the principles of a professional code.
- [ ] I can explain why copyright legislation is needed and what software piracy is.
- [ ] I can describe free software (the Free Software Foundation), open source software (the Open Source Initiative), shareware and commercial software.
- [ ] I can justify a choice of licence for a scenario.
- [ ] I can describe applications of artificial intelligence.
- [ ] I can discuss the social, economic and environmental impact of an AI system, with benefits and concerns.
:::

:::recap
- Ethics means the principles about right and wrong. Computing professionals have extra responsibility because their work reaches many people, who cannot easily check it. Law and ethics differ: an action can be legal but unethical.
- Principles: act in the public interest, be competent, be honest, respect confidentiality, respect ownership, treat people fairly, and meet your duties to employer and profession.
- Professional ethical bodies (BCS, IEEE) set a code of conduct, promote standards and qualifications, support development and give the profession a voice.
- Copyright gives the creator control over copying; it is needed so creators can earn from their work and so others cannot copy it. Software piracy is illegal copying, sharing or use.
- Licences: free software (FSF: freedom to run, study, change and share; "free" means freedom, not price; some are copyleft); open source (OSI: source code available, licence conditions vary); shareware (free trial, then pay); commercial (paid licence, no source code, no copying).
- Justify a licence from the scenario: cost, need to change the program, support, whether the developer wants to earn money or to share, and whether the source code must be secret.
- AI applications: medical diagnosis, autonomous vehicles, fraud detection, translation, recommendations. Impact: social (better services; bias, privacy, accountability), economic (productivity and new jobs; job loss, inequality), environmental (energy savings; electricity and water use, electronic waste).
:::

:::links
- read: [BCS, The Chartered Institute for IT](https://www.bcs.org/) · BCS · the professional body for IT, with its code of conduct
- read: [Approved open source licences](https://opensource.org/licenses) · Open Source Initiative · the licences that meet the Open Source Definition
- read: [ICO for organisations](https://ico.org.uk/for-organisations/) · ICO (UK) · an example of a regulator that explains data protection law
- watch: [Computerphile](https://www.youtube.com/@Computerphile) · Computerphile · short videos on AI, ethics and society
- practise: [Artificial intelligence: exam questions](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/18-artificial-intelligence-ai-/artificial-intelligence-ai/exam-questions/) · Save My Exams · A Level AI questions that also practise describing the impact of AI [paid]

Links checked 13 November 2026.
:::

Next: [Databases: the relational model and normalisation](#cs.databases)
