# COURSE: Other Subjects (other)

Planned by the Organizer (2026-10-03). Re-planned on 2026-10-15: the course now has a Specialist who verifies facts, plans packages and reviews (see below).

## Scope (Organizer re-plan, 2026-10-15)
The user wants every course **comprehensive and really helpful**, at the depth of the finished Maths and Physics
courses. course.json now holds a fuller chapter sketch (23 chapters) built from the syllabus structure. It is a
sketch: check it against the syllabus in LEAD step 2, split any chapter that is still too big, add what is missing,
and keep these ids where you can (aliases for any you rename or merge).
- **Depth:** every topic chapter has every kit/STYLE.md section: worked examples with marks, exam practice ★ to ★★★,
  stretch, quiz, checklist, recap, and a "Learn more online" box.
- **Exam readiness** (the last packages): a guide per paper (or pair of papers), mixed practice for AS and A Level,
  and one mock per written paper, in the real paper's time, marks and question style.
- **Links:** students revise on other sites and apps too, so each topic chapter's `:::links` box sends them to the
  best free ones. LEAD builds the verified link list in COURSE.md (template LEAD step 4).
- **Syllabus years** are in course.json `"years"`. Plan for that syllabus; if the board has published a newer one
  for later exams, add a short note in the overview chapter about what changes.
- **One board** in `:::board` boxes: one board and one content difference you are sure of, or none.

## Notes for this course (re-plan)
- This course now has a **Specialist** (`"lead": true`): LEAD verifies each subject's facts from the boards' own
  subject pages (Cambridge codes and paper structure may be named once they are in FACTS.md with their source),
  plans packages of 2–3 chapters, and reviews like the other courses.
- Each chapter adds to the old list below: **a first study week** (what to do in the first 5 sessions if self-taught),
  the 3–5 hardest topics and why, a short `:::quiz` on what the subject is like, and a "Learn more online" box.
- Computer Science, Psychology and Further Mathematics are full courses now (`cs`, `psych`, and `math.fm.*` in the
  Maths course): other.overview lists them with links, and there are no summary chapters for them here.

## Purpose
Many readers take one or two A Levels outside the big sciences and business. Each chapter is an honest,
practical guide to a subject or a family of subjects, so a student can decide whether to take it and how to
start studying it alone. These are **summary chapters** (`@level sum`), not full courses.

## What each chapter covers (per subject, in this order)
1. What the subject is really like day to day, and who it suits (skills, interests, workload).
2. The main topics, as a short table or list (at A Level standard, board-neutral).
3. How it is assessed: written exams, coursework or non-exam assessment, practical or oral parts,
   described in general terms only.
4. Good combinations with other A Levels, and the university courses and careers it leads to.
5. How to study it well, especially as a self-taught or private candidate (some subjects need a school
   or centre for coursework; say so plainly).
6. Free, reputable resources (official syllabus pages, past papers from the boards, well-known free sites).
Close the chapter with a `:::recap` and a `Next:` line. Use tables, `:::tip`, `:::warn` and `:::exam` boxes.
No `:::try` or `:::quiz` blocks are required, but one short `:::quiz` per chapter is welcome.

## Accuracy rules for this course
- **No syllabus codes, paper numbers, durations or weightings** unless they are in FACTS.md. Describe
  assessment in general terms ("mostly written exams, with an extended essay" etc.) and only when you are sure.
- No numbers that need checking, so `checks/*.py` files are not needed here.
- Be balanced: say what is hard about each subject as well as what is rewarding.

## Chapter scope
| id | Covers |
|---|---|
| other.overview | One large table of every subject in this course and the big courses (what it is in one line, assessment style, pairs well with, chapter link), then how to choose. Written last. |
| other.it | Information Technology |
| other.envm | Environmental Management and Marine Science |
| other.pe | Physical Education |
| other.english | English Literature |
| other.englang | English Language (and the combined English Language and Literature) |
| other.languages | Modern foreign languages (and first-language options) |
| other.classics | Classics, Classical Civilisation and Latin |
| other.history | History |
| other.geography | Geography |
| other.sociology | Sociology |
| other.law | Law |
| other.politics | Politics and Government |
| other.humanities | Religious Studies and Philosophy |
| other.global | Global Perspectives, Thinking Skills and the Extended Project (EPQ) |
| other.arts | Art and Design |
| other.music | Music |
| other.drama | Drama and Theatre |
| other.media | Media Studies and Film Studies |
| other.more | Less common choices at a glance (Travel and Tourism, Design and Technology, Digital Media, and others), one paragraph each |

## Links
Link to the big courses where a subject overlaps (e.g. Computer Science → Mathematics course map,
Psychology → Biology). Grep kit/LINKS.md for ids. Link the core chapters on choosing subjects
(`start.choose`) and studying as a private candidate (`road.private`).

## Model
kit/EXAMPLE.md shows the house formatting (blocks, tone), but it is a full topic chapter; these chapters are
shorter guides. Tone: warm, direct, honest.
