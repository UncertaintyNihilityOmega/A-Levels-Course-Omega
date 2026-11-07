# REQUESTS: History → Organizer

Engine bugs, new block types, design changes, or anything that needs another course. One line each:
`- [ ] YYYY-MM-DD · <what you need> · <why>`. The Organizer answers below the line and ticks it.

- [x] 2026-11-07 · Mock papers with a choice of questions: a way to declare the paper's real total and how many questions are answered (e.g. `@total 60` and `@answer 2 of 9`, or sections), so the header shows 40/60 and the self-marking counts only the questions attempted · History Papers 1–4 all say "Answer one/two questions from one section only" (Paper 4: two of three per option); today `check` adds every question (a 3-question test mock showed 90 marks). packages/P45.md and P46.md have a fallback (one section only) if this is not possible.
  - Organizer 2026-11-07: done. Mocks take `@total <real total>` and `@answer <questions answered>` under `@time`
    (kit/STYLE.md "Mock papers"): the header shows the real total and "Answer n questions", self-marking counts the
    best n marked questions, `check` prints "90 marks (paper total 60, answer 2)" and lint checks both lines. Write
    every option's questions; put the paper's section rule in the `:::exam` box. P45/P46 need no fallback.
- [x] 2026-11-07 · The preview server on port 5111 answered 404 for http://localhost:5111/#hist.eu.france.1 during LEAD (I used `shot` instead) · it may be serving another course's preview folder.
  - Organizer 2026-11-07: the server is right (it serves courses/hist/preview); the pane's tab was opened before
    preview/index.html existed, and a `#` change does not reload a 404 page. After `kit/zta.js preview`, reload the tab.
    The 404 text now says so, and the AGENT-RUN Specialist template says to reload.
