# COURSE: Other Subjects (other)

Planned by the Organizer (2026-10-03). There is no Specialist for this course: a Writer works through the
packages in course.json, and the Organizer reviews the result when assembling the site.

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
| other.overview | One large table of about 25 subjects (subject, what it is in one line, assessment style, pairs well with, chapter link), then how to choose. Write it last in P1. |
| other.cs | Computer Science |
| other.psychology | Psychology |
| other.pe | Physical Education |
| other.more | Information Technology, Environmental Management, Marine Science, Travel and Tourism, the Extended Project (EPQ) and other less common choices |
| other.english | English Language, English Literature, and English Language and Literature |
| other.history | History |
| other.geography | Geography |
| other.sociology | Sociology |
| other.law | Law |
| other.politics | Politics, Global Perspectives and Thinking Skills |
| other.languages | Modern foreign languages (and first-language options) |
| other.arts | Art and Design, Music, Drama and Theatre, Media Studies |
| other.humanities | Religious Studies, Philosophy and Classics |

## Links
Link to the big courses where a subject overlaps (e.g. Computer Science → Mathematics course map,
Psychology → Biology). Grep kit/LINKS.md for ids. Link the core chapters on choosing subjects
(`start.choose`) and studying as a private candidate (`road.private`).

## Model
kit/EXAMPLE.md shows the house formatting (blocks, tone), but it is a full topic chapter; these chapters are
shorter guides. Tone: warm, direct, honest.
