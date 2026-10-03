# SESSION — procedure for every Zero to A* work session

Usage is the scarce resource. Follow this exactly. Read only this file, BRIEF.md and the output of
`python3 tools/status.py`. Do not read HANDOFF.md, AUTHORING.md, src/outline.json or other chapters
unless a step below tells you to.

## Fixed facts
- ROOT (the user's folder, master copy): C:\Users\Uncertainty\Desktop\Claude_Test\Zero to A
- Cloud workbench: /home/claude/zta (rebuilt from ROOT every session)
- Published page: https://claude.ai/artifact/V8KUdftuzroYvq7cp4KPWd (title "Zero to A*")
- There is no shell on the user's PC. Build in the cloud; move files with device_stage_files and
  device_commit_files. Files you commit must first be copied under /mnt/user-data/outputs/zta/.

## Rules
1. One work package per conversation, then stop.
2. No subagents, no parallel agents, no Workflow, no WebSearch, no clarifying questions, no task list.
   One WebFetch of the package's official syllabus is allowed (content packages).
3. Each chapter: ONE Write (the whole chapter) → ONE bash (check, verify numbers, backup, copy) →
   ONE commit. Fix problems with small Edit calls. Never rewrite a chapter to fix a detail and never
   read back a chapter you just wrote.
4. No screenshots in content packages. Widget packages: one tools/wtest.py run per widget; look at the
   phone-dark PNG, and at the desktop PNG only if something seems wrong.
5. Keep tool output short (`| tail -n 20`). Never cat large files.
6. Talk to the user only at the end, in three lines.
7. If the user says usage is high: finish the current chapter, save it, do the end steps, stop.

## Start (4 calls)
1. device_stage_files (one call): ROOT\SESSION.md, ROOT\STATUS.md, ROOT\dist\backup.json,
   ROOT\vendor\node_modules.tgz, ROOT\vendor\latinmodern-math.otf.
   They arrive under "/mnt/user-data/uploads/Zero to A/".
2. One bash:
   U="/mnt/user-data/uploads/Zero to A"; mkdir -p /home/claude/zta && cd /home/claude/zta && python3 -c "import json,os,sys;d=json.load(open(sys.argv[1],encoding='utf-8'))['files'];[(os.makedirs(os.path.dirname(p) or '.',exist_ok=True),open(p,'w',encoding='utf-8').write(t)) for p,t in d.items()];print(len(d),'files restored')" "$U/dist/backup.json" && cp "$U/STATUS.md" STATUS.md && mkdir -p vendor && cp "$U/vendor/latinmodern-math.otf" vendor/ && tar xzf "$U/vendor/node_modules.tgz" && (pip install -q brotli --break-system-packages >/dev/null 2>&1 || true) && python3 tools/status.py | tail -n 14
3. Read /home/claude/zta/BRIEF.md. If status.py names a spec file (e.g. WP0.md), read that too.
4. Content packages: one WebFetch of the syllabus URL printed by status.py with the prompt
   "List compactly, as bullets, every learning outcome for <topics>." Use the list as your coverage checklist.

## Each chapter (3 calls)
1. Write /home/claude/zta/content/<subject>/<chapter-id>.md
   (subject = math, phys, chem, bio, eng, bus, econ (also for acc.*), other, tools).
2. One bash (the heredoc recomputes every number in the chapter and prints only failures):
   cd /home/claude/zta && node tools/check.js content/<subject>/<id>.md | tail -n 12 && python3 - <<'PY'
   # e.g. assert abs(10*3.0*math.cos(math.radians(30)) - 26) < 0.5
   print('numbers OK')
   PY
   python3 tools/backup.py >/dev/null && O=/mnt/user-data/outputs/zta && mkdir -p "$O/content/<subject>" "$O/dist" && cp content/<subject>/<id>.md "$O/content/<subject>/" && cp dist/backup.json "$O/dist/"
3. device_commit_files with force: true:
   /mnt/user-data/outputs/zta/content/<subject>/<id>.md → ROOT\content\<subject>\<id>.md
   /mnt/user-data/outputs/zta/dist/backup.json → ROOT\dist\backup.json

## End (4 calls)
1. One bash: cd /home/claude/zta && node build.js | tail -n 6 && python3 tools/backup.py, then append one
   line to STATUS.md: "- <YYYY-MM-DD> · <WP id> · <what was added> · <notes>" (include "DONE <WP id>"
   when the package is complete), then python3 tools/status.py | tail -n 4, then copy dist/index.html,
   dist/zero-to-a-star.html, dist/backup.json and STATUS.md into /mnt/user-data/outputs/zta/ (same sub-paths).
2. Artifact read: url = the published page, path = "backup.json" (this counts as reading the page; the
   file is saved to disk, not printed).
3. Artifact publish: url = the published page, file_path = /home/claude/zta/dist/index.html,
   files = {"backup.json": "/home/claude/zta/dist/backup.json"}, label = "<WP id>". No icon.
4. device_commit_files (force: true): dist\index.html, dist\zero-to-a-star.html, dist\backup.json, STATUS.md.
Then reply in three lines: what was added, anything uncertain, what is next.

## If something goes wrong
- Publish refused because the page was not read: do one plain Artifact read of it (costly, once), then publish.
- Checker says an id is unknown: use an id from OUTLINE.md (or an alias listed there).
- Widget packages: write the file named by status.py in sections, test each widget with
  `WT_OUT=/tmp/wt python3 tools/wtest.py src/<file>.js 'name|data-…'`, commit the file after each widget.
- Engine edits (WP0 or a fix): commit every changed engine file as well.
