# data/p12_probe.py: probes every widget used in the P12 chapters with the chapter's own attributes
import re, subprocess, sys
for cid in ("hist.us.depression.3", "hist.us.depression.4"):
    src = open(f"chapters/{cid}.md", encoding="utf-8").read()
    for m in re.finditer(r'<div class="widget" data-w="([\w-]+)"([^>]*)></div>', src):
        name, attrs = m.group(1), m.group(2).strip()
        r = subprocess.run(["node", "kit/zta.js", "widget", name, attrs, "--probe"], capture_output=True, text=True, encoding="utf-8")
        out = (r.stdout + r.stderr).strip().splitlines()
        print(f"== {cid} {name}: exit {r.returncode}")
        for line in out[-8:]:
            print("   ", line[:200])
