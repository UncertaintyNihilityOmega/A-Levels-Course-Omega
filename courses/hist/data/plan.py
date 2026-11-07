# data/plan.py: the History chapter plan; rewrites chapters, aliases, packages and papers in course.json
# Run from the course folder: py data/plan.py
import json
C = []  # chapters in course order


def add(i, t, l, g):
    C.append({"id": i, "title": t, "level": l, "group": g})


S, K = "Start here", "History skills"
add("hist.overview", "History: the course map", "guide", S)
add("hist.f.basics", "History from zero: evidence, sources and arguments", "pre", S)
add("hist.f.choose", "Choosing your options and planning the course", "guide", S)
add("hist.skills.sources", "Skills: reading and comparing sources (Paper 1)", "as", K)
add("hist.skills.essays", "Skills: writing the analytical essay (Papers 2 and 4)", "as", K)
EU = "AS European: Modern Europe, 1774–1924"
US = "AS American: the USA, 1820–1941"
INT = "AS International: international history, 1870–1939"
T = {
    "hist.eu.france": (EU, "France", ["the causes and immediate consequences of the 1789 Revolution", "how and why France became a republic by 1792", "governing France, 1793–99: the Terror and the Directory", "the rise and fall of Napoleon Bonaparte"]),
    "hist.eu.germany": (EU, "Germany", ["the causes of the revolutions of 1848", "the 1848–49 revolutions and their consequences", "Bismarck's appointment and his aims to 1866", "how and why unification was achieved by 1871"]),
    "hist.eu.russia": (EU, "Russia", ["the challenges facing Tsarism, 1881–94", "the 1905 Revolution and its outcomes to 1914", "how and why the Bolsheviks seized power in 1917", "how the Bolsheviks consolidated power to 1924"]),
    "hist.us.civilwar": (US, "Civil War and Reconstruction", ["growing tension between North and South before 1860", "why the Civil War broke out in April 1861", "why the Civil War lasted four years", "the aims and success of Reconstruction"]),
    "hist.us.gilded": (US, "Gilded Age and Progressive Era", ["why there was rapid industrialisation after 1870", "the consequences of rapid economic growth", "why the Progressive Movement developed: aims and policies", "how successful the Progressive Movement was, 1890–1920"]),
    "hist.us.depression": (US, "Crash, Depression and New Deal", ["the causes of the Great Crash and the Great Depression", "the impact of the Crash and the Depression, and Hoover's response", "how successful Roosevelt's first New Deal was", "the Second New Deal and its impact by 1941"]),
    "hist.int.empire": (INT, "Imperialism and world powers", ["why imperialism was a significant force in Africa from 1870", "imperial expansion and international relations to 1914", "why Japan emerged as a world power", "why the USA emerged as a world power"]),
    "hist.int.1919": (INT, "International relations, 1919–29", ["dissatisfaction with the peace settlements of 1919–20", "the League of Nations: creation and challenges in the 1920s", "why tensions remained high after Versailles", "how and why relations improved, 1924–29"]),
    "hist.int.1929": (INT, "International history, 1929–39", ["the rise of extremism and international relations", "why the League failed to keep the peace in the 1930s", "appeasement: why, and with what effects", "why war broke out in 1939"]),
}
AS_TOPICS = list(T)


def topic(prefix, lvl):
    g, name, kqs = T[prefix]
    for n, k in enumerate(kqs, 1):
        add(f"{prefix}.{n}", f"{name} ({n}): {k}", lvl, g)


for p in AS_TOPICS:
    topic(p, "as")
P3 = "A Level Paper 3: historical interpretations"
add("hist.interp.skills", "How historians disagree: reading an interpretation", "a2", P3)
add("hist.interp.ww1.1", "Origins of the First World War (1): the road to war, c.1890–1914", "a2", P3)
add("hist.interp.ww1.2", "Origins of the First World War (2): the historians' debate", "a2", P3)
add("hist.interp.holocaust.1", "The Holocaust (1): from antisemitism to genocide", "a2", P3)
add("hist.interp.holocaust.2", "The Holocaust (2): the historians' debate", "a2", P3)
add("hist.interp.coldwar.1", "Origins of the Cold War (1): the breakdown of the wartime alliance, 1941–49", "a2", P3)
add("hist.interp.coldwar.2", "Origins of the Cold War (2): the historians' debate", "a2", P3)
D4E = "A Level Paper 4 European: Europe, 1919–41"
D4A = "A Level Paper 4 American: the USA, 1945–93"
D4I = "A Level Paper 4 International: international history, 1909–94"
T.update({
    "hist.d.italy": (D4E, "Mussolini's Italy", ["how Mussolini gained control", "how effectively Mussolini governed Italy", "how successful Mussolini's economic policies were", "how far Mussolini transformed Italian society"]),
    "hist.d.stalin": (D4E, "Stalin's Russia", ["how Stalin gained control", "how effectively Stalin governed the Soviet Union", "how successful Stalin's economic policies were", "how far Stalin transformed Soviet society"]),
    "hist.d.hitler": (D4E, "Hitler's Germany", ["how Hitler gained control", "how effectively the Nazis governed Germany", "how successful Nazi economic policies were", "how far the Nazis transformed German society"]),
    "hist.d.usa45": (D4A, "Post-war USA, 1945–61", ["Truman and the internal issues of post-war America", "how effective Eisenhower was as President", "economic and social change, 1945–61", "the foreign policies of Truman and Eisenhower"]),
    "hist.d.usa61": (D4A, "A time of challenges, 1961–74", ["the presidencies of Kennedy, Johnson and Nixon", "Cuba and Vietnam", "civil rights for African Americans", "challenges to authority"]),
    "hist.d.usa74": (D4A, "The USA, 1974–93", ["the problems of the late 1970s", "the New Conservatism, 1981–92", "Carter's foreign policies, 1977–81", "changing relations with the USSR"]),
    "hist.d.soviet": (D4I, "The Soviet Empire in Eastern Europe", ["the USSR and the satellite states to 1968", "stagnation, 1964–85", "Gorbachev's response to crisis", "the collapse of Soviet control, 1980–91"]),
    "hist.d.safrica": (D4I, "End of minority rule", ["the apartheid state, 1948–59", "resistance and repression in South Africa, 1960–77", "the end of apartheid, 1978–94", "the end of white minority rule in Zimbabwe, 1965–80"]),
    "hist.d.malaysia": (D4I, "The route to independence", ["nationalism and colonial rule in Malaya to 1945", "the formation of Malaysia", "the Indonesian nationalist movement to 1945", "Indonesia: independence and challenges to the mid-1960s"]),
})
D4 = ["hist.d.italy", "hist.d.stalin", "hist.d.hitler", "hist.d.usa45", "hist.d.usa61", "hist.d.usa74", "hist.d.soviet", "hist.d.safrica", "hist.d.malaysia"]
for p in D4:
    topic(p, "a2")
X = "Exam readiness"
for i, t, l in [("hist.exam.p1", "Paper 1: Historical sources", "guide"), ("hist.exam.p2", "Paper 2: Outline study", "guide"),
                ("hist.exam.p3", "Paper 3: Historical interpretations", "guide"), ("hist.exam.p4", "Paper 4: Depth study", "guide"),
                ("hist.mixed.as", "Mixed practice: AS", "guide"), ("hist.mixed.a2", "Mixed practice: A Level", "guide"),
                ("hist.mock.p1", "Mock Paper 1", "mock"), ("hist.mock.p2", "Mock Paper 2", "mock"),
                ("hist.mock.p3", "Mock Paper 3", "mock"), ("hist.mock.p4", "Mock Paper 4", "mock")]:
    add(i, t, l, X)

# packages: half a topic each in teaching order, then skills, then exam readiness
P = []


def pk(title, ch, w=()):
    P.append({"id": f"P{len(P) + 1}", "title": title, "chapters": ch, "widgets": list(w)})


W = {"hist.eu.france": ["hist-timeline"], "hist.eu.russia": ["hist-chart"]}
for p in AS_TOPICS:
    name = T[p][1]
    pk(f"{name}: key questions 1–2", [f"{p}.1", f"{p}.2"], W.get(p, []))
    pk(f"{name}: key questions 3–4", [f"{p}.3", f"{p}.4"])
pk("Paper 3 skills and the First World War debate", ["hist.interp.skills", "hist.interp.ww1.1", "hist.interp.ww1.2"], ["hist-sort"])
pk("Paper 3: the Holocaust", ["hist.interp.holocaust.1", "hist.interp.holocaust.2"])
pk("Paper 3: the Cold War", ["hist.interp.coldwar.1", "hist.interp.coldwar.2"])
for p in D4:
    name = T[p][1]
    pk(f"{name}: key questions 1–2", [f"{p}.1", f"{p}.2"])
    pk(f"{name}: key questions 3–4", [f"{p}.3", f"{p}.4"])
pk("Start here: course map, foundations and choosing options", ["hist.overview", "hist.f.basics", "hist.f.choose"])
pk("Skills: sources and essays", ["hist.skills.sources", "hist.skills.essays"], ["hist-provenance", "hist-essayplan"])
pk("Exam guides: Papers 1 and 2", ["hist.exam.p1", "hist.exam.p2"], ["hist-levels"])
pk("Exam guides: Papers 3 and 4", ["hist.exam.p3", "hist.exam.p4"])
pk("Mixed practice", ["hist.mixed.as", "hist.mixed.a2"])
pk("Mocks: Papers 1 and 2", ["hist.mock.p1", "hist.mock.p2"])
pk("Mocks: Papers 3 and 4", ["hist.mock.p3", "hist.mock.p4"])
ids = [c["id"] for c in C]
assert len(ids) == len(set(ids)) and sorted(ids) == sorted(x for p in P for x in p["chapters"])
AS_ = [c["id"] for c in C if c["group"] in (EU, US, INT)]
papers = [
    {"id": "P1", "title": "Paper 1: Historical sources", "chapters": ["hist.skills.sources"] + AS_ + ["hist.exam.p1"]},
    {"id": "P2", "title": "Paper 2: Outline study", "chapters": ["hist.skills.essays"] + AS_ + ["hist.exam.p2"]},
    {"id": "P3", "title": "Paper 3: Historical interpretations", "chapters": [c["id"] for c in C if c["group"] == P3] + ["hist.exam.p3"]},
    {"id": "P4", "title": "Paper 4: Depth study", "chapters": ["hist.skills.essays"] + [c["id"] for c in C if c["group"] in (D4E, D4A, D4I)] + ["hist.exam.p4"]},
]
j = json.load(open("course.json", encoding="utf-8"))
j["years"] = "2027–2029"
j["chapters"] = C
j["aliases"] = {"hist.interp.ww1": "hist.interp.ww1.2", "hist.interp.holocaust": "hist.interp.holocaust.2", "hist.interp.coldwar": "hist.interp.coldwar.2"}
j["packages"] = P
j["papers"] = papers
json.dump(j, open("course.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(C), "chapters,", len(P), "packages")
