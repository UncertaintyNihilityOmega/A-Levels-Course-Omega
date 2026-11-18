# data/cs_ai_tables.py: prints the Markdown tables of chapter cs.ai (pasted into the chapter by hand; checks/cs.ai.py compares).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cs_ai_algos import *

def show(title, text):
    print("#", title); print(text); print()

rows, vis, dist, prev = dijkstra(TOWN, "A", "G")
show("town dijkstra", dijkstra_md(rows, sorted(TOWN)))
show("town final", final_md(sorted(TOWN), dist, prev, vis))
rows, cl, g, p = astar(TOWN, TOWN_H, "A", "G")
show("town astar", astar_md(rows))
rows, cl, g, p = astar(GRID, manhattan("F5", GRID), "A1", "F5")
show("grid astar", astar_compact_md(rows))
rows, vis, dist, prev = dijkstra(STOP, "S", "T")
show("stop", dijkstra_md(rows, sorted(STOP)))
rows, vis, dist, prev = dijkstra(Q4, "P", "U")
show("q4 dijkstra", dijkstra_md(rows, sorted(Q4)))
show("q4 final", final_md(sorted(Q4), dist, prev, vis))
rows, cl, g, p = astar(Q5, Q5_H, "H", "N")
show("q5 astar", astar_md(rows))
rows, cl, g, p = astar(EXAM_GRID, manhattan("E4", EXAM_GRID), "A1", "E4")
show("egrid astar", astar_compact_md(rows))
rows, cl, g, p = astar(OVER, OVER_H, "S", "G")
show("over astar", astar_md(rows))
