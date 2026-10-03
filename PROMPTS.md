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
| A problem | `Project Organizer session. Read ORGANIZER.md. <describe the problem>` |

## Courses (folder: `A Levels Course\courses\<c>`)
| Course | Folder | Specialist (Opus) | Writer (Sonnet) |
|---|---|---|---|
| Mathematics | `courses\math` | `Mathematics Specialist: LEAD session. Follow CLAUDE.md.` | `Mathematics Writer: WRITE session. Follow CLAUDE.md.` |
| Physics | `courses\phys` | `Physics Specialist: LEAD session. Follow CLAUDE.md.` | `Physics Writer: WRITE session. Follow CLAUDE.md.` |
| Chemistry | `courses\chem` | `Chemistry Specialist: LEAD session. Follow CLAUDE.md.` | `Chemistry Writer: WRITE session. Follow CLAUDE.md.` |
| Biology | `courses\bio` | `Biology Specialist: LEAD session. Follow CLAUDE.md.` | `Biology Writer: WRITE session. Follow CLAUDE.md.` |
| Engineering | `courses\eng` | `Engineering Specialist: LEAD session. Follow CLAUDE.md.` | `Engineering Writer: WRITE session. Follow CLAUDE.md.` |
| Business | `courses\bus` | `Business Specialist: LEAD session. Follow CLAUDE.md.` | `Business Writer: WRITE session. Follow CLAUDE.md.` |
| Economics | `courses\econ` | `Economics Specialist: LEAD session. Follow CLAUDE.md.` | `Economics Writer: WRITE session. Follow CLAUDE.md.` |
| Accounting | `courses\acc` | `Accounting Specialist: LEAD session. Follow CLAUDE.md.` | `Accounting Writer: WRITE session. Follow CLAUDE.md.` |
| Other Subjects | `courses\other` | (none: planned by the Organizer) | `Other Subjects Writer: WRITE session. Follow CLAUDE.md.` |

For a review, use the Specialist prompt with REVIEW instead of LEAD:
`<Course> Specialist: REVIEW session. Follow CLAUDE.md.`

## The cycle for one course
LEAD (Specialist, once) → WRITE P1 → WRITE P2 → REVIEW → WRITE P3 (fixes first) → WRITE P4 → REVIEW → … →
REVIEW FINAL. Not sure what is next? Any chat in the course folder can run `node kit/zta.js status`, and
`node engine/status.js` at the root shows every course.
