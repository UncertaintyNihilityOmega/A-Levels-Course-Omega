# COURSE: History (hist)

The course plan and rules. Written by the History Specialist in LEAD (2026-11-07). Writers read this file, kit/STYLE.md,
the gold chapter and their own packages/`Pn`.md. Exam facts, mark-scheme levels and every learning outcome are in
FACTS.md (grep it for your topic).

## Scope and board
- Cambridge International AS & A Level History **9489**, syllabus for 2027, 2028 and 2029 (exams June and November).
  `course.json` `"years": "2027–2029"`.
- The course covers **every option**: all three AS options (European, American, International; three topics each),
  all three Paper 3 topics and all three Paper 4 options (three topics each). A student studies one AS option (all
  three of its topics), one Paper 3 topic and at least two topics of one Paper 4 option. hist.f.choose explains this.
- **One chapter per key question.** Each AS and Paper 4 topic has four key questions (KQ) in the syllabus; chapter
  `<topic>.n` covers KQ n in full (FACTS.md lists the content). Each Paper 3 topic has a context chapter (`.1`, the
  events, AO1) and a debate chapter (`.2`, the historians, AO4). 94 chapters in 46 packages.
- Topic rotation (Papers 1 and 2): every AS topic is the Paper 1 sources topic in one year and a Paper 2 essay topic in
  the other two (table in FACTS.md). So **every AS topic chapter teaches both**: Paper 1 source questions and Paper 2
  essay questions, and says in its opening `:::exam` box where it is examined in 2027, 2028 and 2029.
- Main board Cambridge International. `:::board`: one other board and one difference you are sure of (verified, e.g.
  AQA A Level History 7042 has the depth option "2H France in Revolution, 1774–1815", A Level only), or no box.

## Conventions
- Dates: 14 July 1789 (day month year, no ordinal, no comma); decades "the 1920s"; centuries "nineteenth century";
  ranges with an en dash: 1789–92, 1919–29 (year ranges keep two digits after the dash within a century, as the
  syllabus does). "c." for circa: c.1870.
- Names: full name and role at first mention ("Charles-Alexandre de Calonne, Controller-General of Finances"), then the
  surname. Foreign terms in italics with a translation at first use: *cahiers de doléances* (lists of grievances).
  Russian dates: say whether Old Style (Julian) or New Style; give 1917 events in Old Style, as most textbooks do, with the New Style date at first
  mention ("the October Revolution, 25 October 1917 (7 November New Style)").
- Money and numbers: in the period's units (livres, roubles, marks, dollars) with the year; statistics only from a
  named reliable source type and rounded honestly ("about", "roughly"). Where historians' estimates differ, say so and
  give the range. Every number in a chapter goes in `checks/<id>.py` (dates arithmetic, percentages, totals).
  Look up every value of a chart series at its named source, not from memory (review of P28–P31 found two of four
  "BLS" values taken from a different series), and give the latest verdict on a case (two of the three men convicted
  of killing Malcolm X were cleared in 2021).
- Spelling: British (organise, labour, defence) except proper names and quotations ("Department of Labor",
  "American Federation of Labor").
- Terms: use the syllabus's own words (Ancien Régime, *Zollverein*, Sovnarkom, the Great Turn, apartheid, Konfrontasi).

## Depth and tone
- Depth: a student who masters the chapter can write a Level 5 Paper 2 (b) answer or a Level 5 Paper 4 essay on any
  question the key question allows, and evaluate sources on it in context. Cover every "including" item; give dates,
  names, numbers and the reasons behind events, not lists. Long chapters are expected (the gold chapter is the model:
  about 9,000–12,000 words); never cut depth to save effort.
- Explain the history as a story first (what happened, in order), then analyse it (why, how far, how important).
  Every section ends with what it means for the key question.
- Historians: name a historian only when you are sure of the work and its argument (author, title, year). At AS, a
  short `:::note` on the debate is stretch; at A Level (Paper 3) it is the core. Never invent a quotation; quote only
  words you are certain of, and mark adapted or paraphrased extracts as such. Name a critic or reviewer of a book only
  when you have read the criticism, check that a historian was alive and writing when you place him in a debate (review
  of P16–P19: Ritter, who died in 1967, was said to dispute diaries published in 1972), and leave out colourful details
  you cannot source ("the government bought hundreds of copies").
- **Sources** (Paper 1 practice): real documents, briefly quoted or closely paraphrased, each with a provenance line in
  italics in the board's style (*From …, a pamphlet by …, January 1789.*). Any shortened, simplified or translated
  extract says "Adapted from …". A visual source is described in words with its real title, date and maker. Never a
  made-up "primary source" presented as real. If you cannot find a real document you are sure of, use a different one.
  Provenance must name the real recorder and edition (a saying from exile: Las Cases 1823, Montholon 1847, Gourgaud;
  a law: the article number in that law, not in a later constitution). Where the famous wording is a later version
  (Napoleon's 1796 "Soldiers, you are naked" was rewritten on St Helena), say so in the provenance line. Never add a
  sentence to a paraphrase that the speaker did not say (review of P1–P3 found one). A source line that says
  "Shortened; the phrases are the document's own" must contain no words of yours (review of P4–P7 found a paraphrase
  inside one); an extract joined from two documents names both in its provenance; a visual source's title, maker and
  place come from a museum or library catalogue entry, not from memory (a cartoon title was wrong). Prefer the real
  words, found online, to a "summary written for practice". Never put reported speech or a summary inside an extract
  ("He went on to say …", "Coolidge said …", "The writer admits …"): find the real sentence, or give only the verified
  phrase with dots (review of P8–P11 replaced over a dozen such extracts). Check what a famous line was about before
  using it (Hoover's "grass will grow" of 1932 was about cutting the tariff) and who wrote it where (Sumner's
  "liberty, inequality, survival of the fittest" is from "The Challenge of Facts", published 1914, not his 1883 book).
  A shortened extract keeps the document's own order and marks every cut with "…", even when labelled "Adapted"
  (review of P12–P15 found extracts by Bülow, Crowe, Cromer and Huey Long rearranged, and cuts with no dots).
  Online texts of treaties and covenants are often the amended version: quote the wording in force on the date the
  provenance gives (review of P20–P23 found the 1924 text of Covenant Article 12 labelled as 1919). Date loans,
  laws and founding acts from a source, not from the year of the campaign they served (the Morgan loan was 1925).
- `hist-chart`: use `data-type="line"` only when the years are close enough to show a trend; three years twenty years
  apart are bars, and the text says what the chart cannot show.
- **Sensitive topics** (the Terror, slavery and Reconstruction violence, colonial atrocities in the Congo and against
  the Herero, the Holocaust, Stalin's famine and Terror, apartheid, the Indonesian killings of 1965–66): factual,
  respectful, the victims named as people, no graphic detail beyond what the history needs, numbers with their
  sources and ranges. Never present an atrocity as a debate about whether it happened.
- Neutral and balanced on political questions (the syllabus is politically neutral): give each side's case in its
  strongest form and let the evidence decide.
- Tone: warm and direct, short sentences, "you". No filler, no em-dash asides, no hype, no emojis.

## How a History topic chapter is built (adapting kit/STYLE.md for an essay subject)
In this order (the gold chapter shows every part):
1. Header lines. `@paper CAIE 9489 Papers 1 and 2 · European option` (AS) or `CAIE 9489 Paper 4 · European option`
   (A Level) or `CAIE 9489 Paper 3` (interpretations). `@time` realistic (AS KQ chapters 8–10 hours).
2. `:::why`, then an `:::exam Where this is examined` box: the papers and years (rotation from FACTS.md), the question
   styles that can be set on it, and the AOs.
3. **Before you start** + `:::try Warm-up` (3 questions from earlier chapters, each naming its chapter).
4. A **timeline table** (Date | Event, short cells) near the start, and a `hist-timeline` widget where it helps (only
   when widgets/hist-timeline.js exists).
5. Content sections (`##`), story then analysis, each with `:::def` cards for key terms (exam-quality wording), and
   `:::key` boxes for the main arguments to learn ("Three reasons why …", "The case for and against …"). Key people in
   a table (Person | Role | Why they matter) where there are many. A hand SVG where a picture helps (social structure,
   causal links, a map schematic, a chart of data); keep maps schematic and accurate, labelled.
6. `:::eg` worked examples = **exam questions with model answers built level by level** against the real mark-scheme
   levels in FACTS.md: show what a Level 2/3 answer writes, then what moves it up a level, then a top-level answer
   (full paragraphs), with examiner-style commentary naming the level and the mark range. Every AS topic chapter has
   at least: one Paper 2 (a) [10] example, one Paper 2 (b) [20] example, one Paper 1 (a) [15] comparison of two real
   sources, one Paper 1 (b) [25] example (at least a full plan with source evaluation and a top-level paragraph and
   judgement). Paper 4 chapters: two or more [30] essays (one "Assess", one "Evaluate"), with a full Level 5 answer for
   one of them. Paper 3 debate chapters: one full worked answer to a "What can you learn …" extract (the extract is a
   clearly labelled paraphrased summary of a named historian's argument, written for practice).
7. `:::warn` common mistakes, `:::exam` technique, `:::board`, `:::note` for the historians' debate.
8. `:::eg Spot the weak paragraph`: a realistic student paragraph, the level it reaches and why, and the fix.
9. `:::try` recall practice (short questions with full answers), then `:::try Exam practice ★ to ★★★` with 6–8 exam-style
   questions in the real styles (both papers for AS topics), each `Q: [n marks] ★★ …`, with 2–3 `H:` hints on ★★★
   questions; each `A:` gives the indicative content (support / challenge / evaluation) and says what a top-level answer
   does. **No mark tokens** in History answers (no [M1], [B1]); write "Level 4 (13–16)" in words. Then
   `:::try Stretch for A*` (1–2 questions, hints, full answers).
10. `:::quiz` (8 or more; wrong options are real misconceptions: wrong dates, wrong causes, confused people),
    `:::checklist What you can now do` (one line per syllabus bullet), `:::recap`, `:::links` (from the list below,
    3–6 links, at least one practise or papers link and one read or watch link, ending with the "Links checked" line),
    then `Next: [Title](#id)`.
- `checks/<id>.py` for every chapter: dates, ages, intervals, percentages, totals and mark totals used in the text.
- Practice and worked questions use only the real command forms of the paper: Paper 4 "Assess …" or "'…' Evaluate
  this view." (never "How far do you agree?", "To what extent …?" or a mixed "… ? Evaluate this view."). Never name
  course files (FACTS.md, COURSE.md) in student-facing text. When two statistics are compared (literacy, census
  shares), take both from the same series and age base, and state the base.
- Connections (user's request, 2026-11-11, after a history student's feedback that topics felt cut off from each
  other): every topic and debate chapter has one `:::note Connections` box just before the `:::checklist`. It holds 3–5
  bullets, `- [Short title](#chapter-id): one sentence` naming a real link (a cause, a consequence, a comparison,
  the same years seen from another country). At least two bullets go outside the chapter's own topic, and at least one
  goes outside its option or paper (e.g. Mussolini's rise → Hitler's Germany (1); Stalin's Five-Year Plans → the
  Depression in the USA; the 1848 revolutions → France). Link only ids in course.json. Add one bullet to
  [The big picture](#hist.f.eras), and for Italy, Stalin and Hitler chapters also
  [Dictatorships compared](#hist.d.compare). Say in one line that students need only their own options' chapters.

## Widgets (each belongs to one package; use another package's widget only when its file exists in widgets/)
- `hist-timeline` (P1): `data-title="…" data-events="1787-02-22 | Assembly of Notables opens | Calonne's reform plan ;; 1789-07-14 | Bastille stormed | …"`
  optional `data-lanes="Politics,Economy,People"` and a fourth field per event naming its lane. Events separated by
  ` ;; `, fields by ` | `; dates YYYY, YYYY-MM or YYYY-MM-DD. Shows a scrollable, keyboard-steppable timeline with the
  selected event's detail; a filter by lane; works at 360 px.
- `hist-chart` (P5): `data-title data-unit data-series="Coal (million tonnes): 1880=3.3, 1890=6.0 ;; Pig iron …" data-source="…"`
  line or bar chart of historical statistics, one or two series, with a table toggle for screen readers and the
  source shown under the chart.
- `hist-sort` (P19): `data-cats="Intentionalist,Functionalist,Structuralist" data-items="Text | Category ;; …"`: sort
  statements into categories with buttons (no dragging needed), then check with explanations.
- `hist-provenance` (P41): source-evaluation trainer (nature, origin, purpose, context → stronger or weaker as evidence
  for a given question), data-driven like hist-sort.
- `hist-essayplan` (P41): essay-plan builder: given a question, place factors as support or challenge, rank them,
  choose a judgement; prints the plan as a paragraph outline.
- `hist-levels` (P42): mark-band explorer: choose the paper and part, tick what an answer does, see the level and
  mark range from FACTS.md's descriptors.
- Shared widgets `planner` and `timer` exist everywhere (use in guides and mocks).

## Mock papers
One per written paper, the real time and total (FACTS.md): Paper 1 1 h 15 min, 40; Paper 2 1 h 45 min, 60; Paper 3
1 h 15 min, 40; Paper 4 1 h 45 min, 60. Original questions in the board's style, sources real and labelled, the 2027
rotation for Papers 1 and 2. The kit adds every question's marks into the header total: choice papers are an open
REQUESTS.md item; the mock packages say what to do.

## Gold chapter
**hist.eu.france.1** (France (1): the causes and immediate consequences of the 1789 Revolution). Read it before you
write: it shows every section, the level-by-level model answers, the source rules and the `:::links` format.

## Packages
46 packages in course.json: P1–P18 the AS topics (two packages per topic: KQ 1–2, KQ 3–4), P19–P21 Paper 3, P22–P39
the Paper 4 topics, P40 Start here, P41 Skills, P42–P43 paper guides, P44 mixed practice, P45–P46 mocks. Each
packages/`Pn`.md is self-sufficient. P1 contains the gold chapter (already written): its Writer writes hist.eu.france.2
and the hist-timeline widget only.

## Verified links for `:::links` (use only these; `[paid]` and `[unofficial]` tags as shown)
Exam (every chapter can use one):
- papers: [Cambridge 9489 past papers and specimen papers](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-history-9489/past-papers/) · Cambridge International · official specimen papers, mark schemes and recent papers
- read: [Cambridge 9489 syllabus page](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-history-9489/) · Cambridge International · the syllabus and its key questions
- practise: [CIE A Level History revision](https://www.savemyexams.com/a-level/history/cie/) · Save My Exams · notes and exam questions by topic [paid]

Primary sources and general:
- explore: [Internet Modern History Sourcebook](https://sourcebooks.fordham.edu/mod/modsbook.asp) · Fordham University · documents by topic. Sections: [French Revolution](https://sourcebooks.fordham.edu/mod/modsbook13.asp), [1848](https://sourcebooks.fordham.edu/mod/modsbook19.asp), [19C Austria and Germany](https://sourcebooks.fordham.edu/mod/modsbook22.asp), [US Civil War](https://sourcebooks.fordham.edu/mod/modsbook27.asp), [Imperialism](https://sourcebooks.fordham.edu/mod/modsbook34.asp), [WWI](https://sourcebooks.fordham.edu/mod/modsbook38.asp), [Russian Revolution](https://sourcebooks.fordham.edu/mod/modsbook39.asp), [The Depression](https://sourcebooks.fordham.edu/mod/modsbook41.asp), [Fascism in Europe](https://sourcebooks.fordham.edu/mod/modsbook42.asp), [Nazism](https://sourcebooks.fordham.edu/mod/modsbook43.asp), [Holocaust](https://sourcebooks.fordham.edu/mod/modsbook44.asp), [Cold War](https://sourcebooks.fordham.edu/mod/modsbook46.asp), [US Power 1945–1990](https://sourcebooks.fordham.edu/mod/modsbook47.asp), [US Society 1945–1990](https://sourcebooks.fordham.edu/mod/modsbook48.asp)
- explore: [The Avalon Project](https://avalon.law.yale.edu/) · Yale Law School · treaties and documents in full; [Declaration of the Rights of Man](https://avalon.law.yale.edu/18th_century/rightsof.asp); [Treaty of Versailles and the peace settlements](https://avalon.law.yale.edu/subject_menus/versailles_menu.asp)
- explore: [Education resources](https://www.nationalarchives.gov.uk/education/) · The National Archives (UK) · document-based lessons
- read: [Milestone documents](https://www.archives.gov/milestone-documents/list) · US National Archives · key US documents with transcripts
- read: [Spartacus Educational](https://spartacus-educational.com/) · Spartacus · encyclopedia entries with extracts [unofficial]

France: [Liberty, Equality, Fraternity: Exploring the French Revolution](https://revolution.chnm.org/) · George Mason University and American Social History Project · documents, images and essays ·
[Napoleon.org](https://www.napoleon.org/en/) · Fondation Napoléon · articles and documents ·
[French Revolution](https://en.wikipedia.org/wiki/French_Revolution) · Wikipedia · overview with references
Germany: [Unification of Germany](https://en.wikipedia.org/wiki/Unification_of_Germany) · Wikipedia ·
[German revolutions of 1848–1849](https://en.wikipedia.org/wiki/German_revolutions_of_1848%E2%80%931849) · Wikipedia
Russia and the USSR: [Seventeen Moments in Soviet History](https://soviethistory.msu.edu/) · Michigan State University · sources year by year from 1917 ·
[Russian Revolution](https://en.wikipedia.org/wiki/Russian_Revolution) · Wikipedia
USA, 1820–1941: [The American Yawp](https://www.americanyawp.com/) · Stanford University Press (free online textbook) ·
[U.S. History](https://openstax.org/details/books/us-history) · OpenStax · free textbook ·
[Digital History](https://www.digitalhistory.uh.edu/era.cfm) · University of Houston · eras, documents ·
[Learn: Civil War](https://www.battlefields.org/learn) · American Battlefield Trust · articles, maps, videos ·
[The Civil War](https://www.nps.gov/civilwar/index.htm) · US National Park Service ·
[Gilded Age](https://en.wikipedia.org/wiki/Gilded_Age) and [Progressive Era](https://en.wikipedia.org/wiki/Progressive_Era) · Wikipedia ·
[FDR Library](https://www.fdrlibrary.org/) · Franklin D. Roosevelt Presidential Library ·
[US History](https://www.khanacademy.org/humanities/us-history) · Khan Academy · videos and practice (watch) ·
[Crash Course US History](https://www.youtube.com/playlist?list=PL8dPuuaLjXtMwmepBjTSG593eG7ObzO7s) · Crash Course (YouTube) · short video overviews (watch)
International 1870–1939: [Scramble for Africa](https://en.wikipedia.org/wiki/Scramble_for_Africa) · Wikipedia ·
[Meiji Restoration](https://en.wikipedia.org/wiki/Meiji_Restoration) · Wikipedia ·
[Asia for Educators](https://afe.easia.columbia.edu/) · Columbia University · Japan and East Asia with sources ·
[Milestones in US foreign relations](https://history.state.gov/milestones) · US Office of the Historian ·
[The League of Nations](https://www.ungeneva.org/en/about/league-of-nations/overview) · UN Geneva ·
[LONTAD: League of Nations archives](https://libraryresources.unog.ch/lontad) · UN Library Geneva ·
[Appeasement](https://en.wikipedia.org/wiki/Appeasement) · Wikipedia ·
[The National WWII Museum](https://www.nationalww2museum.org/) · New Orleans
Paper 3: [National WWI Museum and Memorial](https://www.theworldwar.org/) ·
[Fritz Fischer](https://en.wikipedia.org/wiki/Fritz_Fischer) · Wikipedia ·
[Holocaust Encyclopedia](https://encyclopedia.ushmm.org/) · United States Holocaust Memorial Museum ·
[USHMM](https://www.ushmm.org/) · [Holocaust Denial on Trial](https://www.hdot.org/) · Emory University ·
[Anne Frank House](https://www.annefrank.org/en/) · [Holocaust Educational Trust](https://www.het.org.uk/) ·
[Functionalism versus intentionalism](https://en.wikipedia.org/wiki/Functionalism_versus_intentionalism) · Wikipedia ·
[Historiography of the Cold War](https://en.wikipedia.org/wiki/Historiography_of_the_Cold_War) · Wikipedia ·
[National Security Archive](https://nsarchive.gwu.edu/) · George Washington University · declassified documents
Paper 4 Europe: [Fascist Italy](https://en.wikipedia.org/wiki/Fascist_Italy) · Wikipedia · Seventeen Moments (above) ·
Holocaust Encyclopedia (above, for Nazi Germany)
Paper 4 USA 1945–93: [US Presidents](https://millercenter.org/president) · Miller Center, University of Virginia ·
[Truman Library](https://www.trumanlibrary.gov/) · [Eisenhower Library](https://www.eisenhowerlibrary.gov/) ·
[Carter Library](https://www.jimmycarterlibrary.gov/) · [Reagan Library](https://www.reaganlibrary.gov/) ·
[King Institute](https://kinginstitute.stanford.edu/) · Stanford University · Martin Luther King Jr papers and encyclopedia ·
Milestones in US foreign relations and the National Security Archive (above)
Paper 4 International: [South African History Online](https://www.sahistory.org.za/) ·
[Nelson Mandela Foundation](https://www.nelsonmandela.org/) · [Apartheid](https://en.wikipedia.org/wiki/Apartheid) · Wikipedia ·
[Rhodesian Bush War](https://en.wikipedia.org/wiki/Rhodesian_Bush_War) · Wikipedia ·
[Revolutions of 1989](https://en.wikipedia.org/wiki/Revolutions_of_1989) · Wikipedia ·
[Malayan Emergency](https://en.wikipedia.org/wiki/Malayan_Emergency) · [Formation of Malaysia](https://en.wikipedia.org/wiki/Formation_of_Malaysia) ·
[Indonesian National Revolution](https://en.wikipedia.org/wiki/Indonesian_National_Revolution) · Wikipedia ·
[National Archives of Malaysia](https://www.arkib.gov.my/ms/) (in Malay)

Kinds: archives and sourcebooks are `explore`; encyclopedias, textbooks and Wikipedia are `read`; Khan Academy and
Crash Course are `watch`; Save My Exams is `practise` [paid]; Cambridge past papers are `papers`. A Wikipedia link is
never the only `read` link when a non-Wikipedia one fits. Checked with curl (HTTP 200) on 7 November 2026. Not
reachable from the checker, so not used: Wilson Center Digital Archive, GHDI, Alpha History, Britannica, IWM, Library
of Congress, Yad Vashem (blocked or timed out). End every `:::links` block with: `Links checked 7 November 2026.`
