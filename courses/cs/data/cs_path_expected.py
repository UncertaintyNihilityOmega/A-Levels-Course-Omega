# data/cs_path_expected.py: writes data/cs-path.expected.json, the answers of the chapter's Python (data/cs_ai_algos.py) for every
# start and goal pair of the two widget graphs and both algorithms. data/cs-path.test.js compares the widget's JavaScript with it.
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cs_ai_algos import *  # noqa: E402,F403

out = {}
for gid, adj, hfun in (("town", TOWN, lambda goal: straight_line(TOWN_POS, goal)),
                       ("grid", WIDGET_GRID, lambda goal: manhattan(goal, WIDGET_GRID))):
    out[gid] = {"dijkstra": {}, "astar": {}}
    for s in sorted(adj):
        for g in sorted(adj):
            rows, vis, dist, prev = dijkstra(adj, s, g)
            out[gid]["dijkstra"][f"{s}-{g}"] = {"order": vis, "cost": dist[g], "path": trace_path(prev, g)}
            rows, cl, gg, p = astar(adj, hfun(g), s, g)
            out[gid]["astar"][f"{s}-{g}"] = {"order": cl, "cost": gg[g], "path": trace_path(p, g)}
pathlib.Path(__file__).resolve().parent.joinpath("cs-path.expected.json").write_text(json.dumps(out), encoding="utf-8")
print("pairs", {gid: len(v["astar"]) for gid, v in out.items()})
