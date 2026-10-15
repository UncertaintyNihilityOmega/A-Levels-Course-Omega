# PROMPTS: copy-paste prompts for every chat

Open each chat as described in PROJECT.md ("How to start a course chat"). The folder decides the course, the
prompt decides the role, and the course's CLAUDE.md explains the rest. One chat = one step; close it when it
reports back.

## Organizer (Opus, folder: the project root `A Levels Course`)
| Step | Prompt |
|---|---|
| O2 redesign | `Project Organizer session: phase O2. Read ORGANIZER.md and REORG-PLAN.md and carry out "O2 — Redesign pass".` |
| O3 hand-off | `Project Organizer session: phase O3. Read ORGANIZER.md and REORG-PLAN.md and carry out "O3 — Hand-off".` |
| Assemble | `Project Organizer session: assembly. Read ORGANIZER.md and STATUS.md and run the assembly session.` |
| Agent run | `Project Organizer session: agent run for <Course>. Read ORGANIZER.md and AGENT-RUN.md and build the course with agents until it is done or the usage limit stops it.` |
| Continue a run | `Continue the agent run.` (in the same chat, after a usage-limit stop) |
| A problem | `Project Organizer session. Read ORGANIZER.md. <describe the problem>` |

Classic method or agent method? See PROJECT.md, "Two ways to build a course". The course prompts below are the
classic method. An agent run uses only the "Agent run" prompt above, in one Organizer chat at the project root.

## Courses (folder: `A Levels Course\courses\<c>`)
| Course | Folder | Specialist (Opus) | Writer (Sonnet) |
|---|---|---|---|
| Mathematics | `courses\math` | `Mathematics Specialist: LEAD session. Follow CLAUDE.md.` | `Mathematics Writer: WRITE session. Follow CLAUDE.md.` |
| Physics | `courses\phys` | `Physics Specialist: LEAD session. Follow CLAUDE.md.` | `Physics Writer: WRITE session. Follow CLAUDE.md.` |
| Chemistry | `courses\chem` | `Chemistry Specialist: LEAD session. Follow CLAUDE.md.` | `Chemistry Writer: WRITE session. Follow CLAUDE.md.` |
| Biology | `courses\bio` | `Biology Specialist: LEAD session. Follow CLAUDE.md.` | `Biology Writer: WRITE session. Follow CLAUDE.md.` |
| Computer Science | `courses\cs` | `Computer Science Specialist: LEAD session. Follow CLAUDE.md.` | `Computer Science Writer: WRITE session. Follow CLAUDE.md.` |
| Psychology | `courses\psych` | `Psychology Specialist: LEAD session. Follow CLAUDE.md.` | `Psychology Writer: WRITE session. Follow CLAUDE.md.` |
| Economics | `courses\econ` | `Economics Specialist: LEAD session. Follow CLAUDE.md.` | `Economics Writer: WRITE session. Follow CLAUDE.md.` |
| Business | `courses\bus` | `Business Specialist: LEAD session. Follow CLAUDE.md.` | `Business Writer: WRITE session. Follow CLAUDE.md.` |
| Accounting | `courses\acc` | `Accounting Specialist: LEAD session. Follow CLAUDE.md.` | `Accounting Writer: WRITE session. Follow CLAUDE.md.` |
| Engineering | `courses\eng` | `Engineering Specialist: LEAD session. Follow CLAUDE.md.` | `Engineering Writer: WRITE session. Follow CLAUDE.md.` |
| Other Subjects | `courses\other` | `Other Subjects Specialist: LEAD session. Follow CLAUDE.md.` | `Other Subjects Writer: WRITE session. Follow CLAUDE.md.` |

For a review, use the Specialist prompt with REVIEW instead of LEAD:
`<Course> Specialist: REVIEW session. Follow CLAUDE.md.`
When `status` lists READER (every package reviewed): `<Course> Reader: READER session. Follow CLAUDE.md.` (one chat per 6–8 chapters, one at a time).

## The cycle for one course
LEAD (Specialist, once) → Writers claim packages (2–3 chapters each) → REVIEW when 2+ are written → FIX → … →
READER (in batches) → FIX → REVIEW FINAL. Several Writer chats can run at the same time in the same course folder: each runs
`node kit/zta.js claim` and gets a different package (up to 4 packages ahead of the last review). Use the same
Writer prompt for each. Not sure what is next? Any chat in the course folder can run `node kit/zta.js status`,
and `node engine/status.js` at the root shows every course.

Start a fresh chat (or /clear) for every step: each message re-sends the whole chat, so long chats cost the most.
