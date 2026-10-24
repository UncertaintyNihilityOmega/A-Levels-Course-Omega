# PROMPTS: copy-paste prompts

One chat = one step; close it when it reports back. The folder decides the course, the prompt decides the role, and
the course's CLAUDE.md explains the rest.

## Organizer (Opus, folder: the project root `A Levels Course`)

| Step | Prompt |
|---|---|
| Next roadmap step | `Project Organizer session. Read ORGANIZER.md and ROADMAP.md and take the next step.` |
| Agent run | `Project Organizer session: agent run for <Course>. Read ORGANIZER.md, ROADMAP.md and AGENT-RUN.md and build the course with agents until it is done or the usage limit stops it.` |
| Continue a run | `Continue the agent run.` (same chat, after a usage-limit stop) |
| Assembly | `Project Organizer session: assembly. Read ORGANIZER.md and ROADMAP.md and run the assembly session.` |
| A problem | `Project Organizer session. Read ORGANIZER.md. <describe the problem>` |

## Course chats (classic method; folder: `A Levels Course\courses\<c>`)

1. New session in the Code tab → folder `courses\<c>` (not the project root); decline a worktree.
2. Model: **Opus** for Specialist, **Sonnet** for Writer and Reader.
3. Paste one prompt:

| Role | Prompt |
|---|---|
| Specialist | `<Course> Specialist: LEAD session. Follow CLAUDE.md.` (or `REVIEW session`) |
| Writer | `<Course> Writer: WRITE session. Follow CLAUDE.md.` |
| Reader | `<Course> Reader: READER session. Follow CLAUDE.md.` |

`<Course>` is the course title: Mathematics, Physics, Chemistry, Biology, Computer Science, Engineering, Economics,
Business, Accounting, Psychology, Other Subjects. Any chat can run `node kit/zta.js status` to see the next step.
Several Writer chats can run at once: each claims its own package.
