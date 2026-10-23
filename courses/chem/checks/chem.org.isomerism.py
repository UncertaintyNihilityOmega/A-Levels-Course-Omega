# checks/chem.org.isomerism.py: recomputes every number and every yes/no claim in Isomerism.
# Isomer counts come from brute-force enumeration of carbon skeletons (trees); chiral centres and
# cis-trans from a small SMILES parser. Ar values from data/elements.json (H 1.0, C 12.0, O 16.0).
import json
from itertools import product
from math import isclose

n = 0
def eq(label, got, want, tol=1e-9):
    global n
    n += 1
    assert isclose(got, want, rel_tol=0, abs_tol=tol), f"{label}: computed {got}, chapter says {want}"

def sf(x, k=3):
    return float(f"{x:.{k}g}")

Ar = {e['sym']: e['ar'] for e in json.load(open('data/elements.json', encoding='utf-8'))}
H, C, O = Ar['H'], Ar['C'], Ar['O']

# ---------------------------------------------------------------- carbon skeleton enumeration
def rooted(adj, r, p, mark):
    return '(' + ''.join(sorted(rooted(adj, c, r, mark) for c in adj[r] if c != p)) + ('*' if r == mark else '') + ')'

def canon(adj, mark=None):
    return min(rooted(adj, r, -1, mark) for r in adj)

def trees(k):
    """all carbon skeletons (unrooted trees, max degree 4) with k carbons, as adjacency dicts, up to isomorphism"""
    if k == 1:
        return [{0: []}]
    seen, out = set(), []
    for seq in product(range(k), repeat=k - 2):
        deg = [1] * k
        for s in seq:
            deg[s] += 1
        edges = []
        d = deg[:]
        for s in seq:
            leaf = min(i for i in range(k) if d[i] == 1)
            edges.append((leaf, s)); d[leaf] -= 1; d[s] -= 1
        u, v = [i for i in range(k) if d[i] == 1]
        edges.append((u, v))
        if max(deg) > 4:
            continue
        adj = {i: [] for i in range(k)}
        for a, b in edges:
            adj[a].append(b); adj[b].append(a)
        c = canon(adj)
        if c not in seen:
            seen.add(c); out.append(adj)
    return out

def vertex_orbits(adj, cond=lambda v: True):
    return {canon(adj, v) for v in adj if cond(v)}

def edge_orbits(adj):
    res = {}
    for a in adj:
        for b in adj[a]:
            if a < b:
                adj2 = {k: list(v) for k, v in adj.items()}
                m = len(adj2)
                adj2[m] = [a, b]
                adj2[a].remove(b); adj2[b].remove(a)
                adj2[a].append(m); adj2[b].append(m)
                res.setdefault(canon(adj2, m), (a, b))
    return list(res.values())

def end_groups(adj, u, v):
    """substituents of sp2 carbon u in a double bond u=v: carbon branches and H"""
    subs = [rooted(adj, c, u, None) for c in adj[u] if c != v]
    subs += ['H'] * (2 - len(subs))
    return subs

def alkenes(k):
    """structural alkene isomers with k carbons: list of (adjacency, edge, shows_cis_trans)"""
    out = []
    for adj in trees(k):
        for (a, b) in edge_orbits(adj):
            if len(adj[a]) > 3 or len(adj[b]) > 3:
                continue
            ga, gb = end_groups(adj, a, b), end_groups(adj, b, a)
            out.append((adj, (a, b), len(set(ga)) == 2 and len(set(gb)) == 2))
    return out

# ---- chain isomers of the alkanes
eq("C4H10 isomers", len(trees(4)), 2)
eq("C5H12 isomers", len(trees(5)), 3)
eq("C6H14 isomers", len(trees(6)), 5)
eq("C5H12 H count", 2 * 5 + 2, 12)

# ---- C4H9Br: monosubstituted skeletons
eq("C4H9Br isomers", sum(len(vertex_orbits(t)) for t in trees(4)), 4)
# chiral: only 2-bromobutane (checked below)

# ---- C3H8O: alcohols (OH on a skeleton carbon) + ethers (R-O-R' with 3 carbons in all)
alc = sum(len(vertex_orbits(t)) for t in trees(3))
ethers = sum(1 for a in range(1, 3) for b in range(a, 3) if a + b == 3)      # (1,2): methoxyethane
eq("C3H8O alcohols", alc, 2); eq("C3H8O ethers", ethers, 1); eq("C3H8O isomers", alc + ethers, 3)
eq("C3H8O fits CnH2n+2", 2 * 3 + 2, 8)

# ---- C4H8: alkenes (+ stereo) and rings
al4 = alkenes(4)
eq("C4H8 structural alkenes", len(al4), 3)
stereo4 = sum(2 if cis else 1 for (_, _, cis) in al4)
eq("C4H8 alkene stereoisomers", stereo4, 4)
rings4 = 2    # cyclobutane, methylcyclopropane (the only rings of 4 carbons)
eq("C4H8 total", stereo4 + rings4, 6)
eq("C4H10 minus C4H8", (2 * 4 + 2) - 8, 2)

# ---- C5H10 alkenes
al5 = alkenes(5)
eq("C5H10 structural alkenes", len(al5), 5)
eq("C5H10 stereoisomer total", sum(2 if cis else 1 for (_, _, cis) in al5), 6)
eq("C5H10 with cis-trans", sum(1 for (_, _, cis) in al5 if cis), 1)

# ---- C4H8O carbonyl compounds: aldehydes at a degree-1 skeleton carbon, ketones at a degree-2 carbon
ald = sum(len(vertex_orbits(t, lambda v, t=t: len(t[v]) == 1)) for t in trees(4))
ket = sum(len(vertex_orbits(t, lambda v, t=t: len(t[v]) == 2)) for t in trees(4))
eq("C4H8O aldehydes", ald, 2); eq("C4H8O ketones", ket, 1)

# ---- C3H6O2: acid on a skeleton end (3 carbons) + esters with a+1+b = 3 carbons
acid = sum(len(vertex_orbits(t, lambda v, t=t: len(t[v]) == 1)) for t in trees(3))
esters = sum(1 for a in range(0, 3) for b in range(1, 3) if a + 1 + b == 3)
eq("C3H6O2 acids", acid, 1); eq("C3H6O2 esters", esters, 2)

# ---------------------------------------------------------------- tiny SMILES parser
VAL = {'C': 4, 'O': 2, 'N': 3, 'F': 1, 'Cl': 1, 'Br': 1}

def parse(smi):
    atoms, bonds = [], {}
    stack, prev, order, rings = [], None, 1, {}
    i = 0
    while i < len(smi):
        ch = smi[i]
        if ch in '=#':
            order = {'=': 2, '#': 3}[ch]; i += 1; continue
        if ch == '(':
            stack.append(prev); i += 1; continue
        if ch == ')':
            prev = stack.pop(); i += 1; continue
        if ch.isdigit():
            if ch in rings:
                a, o = rings.pop(ch)
                bonds[frozenset((a, prev))] = max(o, order); order = 1
            else:
                rings[ch] = (prev, order); order = 1
            i += 1; continue
        el = smi[i:i + 2] if smi[i:i + 2] in ('Cl', 'Br') else ch
        i += len(el)
        atoms.append(el)
        idx = len(atoms) - 1
        if prev is not None:
            bonds[frozenset((prev, idx))] = order
        prev, order = idx, 1
    # implicit hydrogens
    nbr = {k: [] for k in range(len(atoms))}
    for b, o in bonds.items():
        a, c = tuple(b)
        nbr[a].append((c, o)); nbr[c].append((a, o))
    mol = {'el': list(atoms), 'nbr': nbr}
    for k, el in enumerate(list(atoms)):
        used = sum(o for _, o in nbr[k])
        for _ in range(VAL[el] - used):
            atoms.append('H'); m = len(atoms) - 1
            nbr[k].append((m, 1)); nbr[m] = [(k, 1)]
    mol['el'] = atoms
    return mol

def sig(mol, a, frm, depth, path):
    if depth == 0:
        return (mol['el'][a],)
    kids = []
    for (b, o) in mol['nbr'][a]:
        if b == frm:
            continue
        if b in path:
            kids.append((o, 'ring', mol['el'][b]))
        else:
            kids.append((o, sig(mol, b, a, depth - 1, path | {a})))
    return (mol['el'][a], tuple(sorted(kids, key=repr)))

def chiral_centres(smi):
    m = parse(smi)
    out = []
    for a, el in enumerate(m['el']):
        if el != 'C' or len(m['nbr'][a]) != 4 or any(o != 1 for _, o in m['nbr'][a]):
            continue
        sigs = [sig(m, b, a, 7, {a}) for (b, _) in m['nbr'][a]]
        if len(set(sigs)) == 4:
            out.append(a)
    return out

def cis_trans_alkene(smi):
    m = parse(smi)
    found = 0
    for a in range(len(m['el'])):
        for (b, o) in m['nbr'][a]:
            if a < b and o == 2 and m['el'][a] == 'C' and m['el'][b] == 'C':
                ga = [sig(m, c, a, 7, {a, b}) for (c, _) in m['nbr'][a] if c != b]
                gb = [sig(m, c, b, 7, {a, b}) for (c, _) in m['nbr'][b] if c != a]
                if len(ga) == 2 and len(gb) == 2 and ga[0] != ga[1] and gb[0] != gb[1]:
                    found += 1
    return found > 0

def ring_cis_trans(smi):
    """True if at least two ring carbons each carry one H and one non-H, non-ring group"""
    m = parse(smi)
    ring_atoms = set()
    # ring atoms: atoms whose removal path returns - simple test: atom in a cycle via DFS
    for a in range(len(m['el'])):
        if m['el'][a] != 'C':
            continue
        # BFS from a avoiding the direct edge back, see whether a is reachable again
        for (b, _) in m['nbr'][a]:
            seen = {a}
            todo = [(b, a)]
            ok = False
            while todo:
                x, p = todo.pop()
                if x == a and p != a:
                    ok = True; break
                if x in seen:
                    continue
                seen.add(x)
                for (y, _) in m['nbr'][x]:
                    if y != p:
                        todo.append((y, x))
            if ok:
                ring_atoms.add(a)
    count = 0
    for a in ring_atoms:
        others = [b for (b, _) in m['nbr'][a] if b not in ring_atoms]
        hs = [b for b in others if m['el'][b] == 'H']
        non_h = [b for b in others if m['el'][b] != 'H']
        if len(hs) == 1 and len(non_h) == 1:
            count += 1
    return count >= 2

# ---- chiral centres
cases = {
    'butan-2-ol': ('CCC(O)C', 1), 'lactic acid': ('CC(O)C(=O)O', 1), 'alanine': ('CC(N)C(=O)O', 1),
    'threonine': ('CC(O)C(N)C(=O)O', 2), '2-chlorobutane': ('CCC(Cl)C', 1), '2-chloropropane': ('CC(Cl)C', 0),
    '3-methylhexane': ('CCC(C)CCC', 1), '2-methylbutane': ('CC(C)CC', 0), 'propan-2-ol': ('CC(O)C', 0),
    'butan-1-ol': ('CCCCO', 0), '2-methylpropan-2-ol': ('CC(C)(C)O', 0), 'propan-1-ol': ('CCCO', 0),
    'pent-3-en-2-ol': ('CC(O)C=CC', 1), '4-methylhex-2-ene': ('CC=CC(C)CC', 1),
    '2-methylcyclohexanone': ('CC1CCCCC1=O', 1), 'methylcyclohexane': ('CC1CCCCC1', 0),
    '2-bromobutane': ('CCC(Br)C', 1), '1-bromobutane': ('CCCCBr', 0), '1-bromo-2-methylpropane': ('CC(C)CBr', 0),
    '2-bromo-2-methylpropane': ('CC(C)(C)Br', 0), 'ethanal + HCN product': ('CC(O)C#N', 1),
    'but-1-ene': ('C=CCC', 0), 'pent-2-ene': ('CC=CCC', 0),
}
for name, (smi, want) in cases.items():
    eq("chiral centres " + name, len(chiral_centres(smi)), want)

# ---- cis-trans in alkenes
ct = {'but-1-ene': ('C=CCC', False), 'but-2-ene': ('CC=CC', True), 'pent-2-ene': ('CC=CCC', True),
      '2-methylbut-2-ene': ('CC(C)=CC', False), '2-methylpropene': ('CC(C)=C', False), 'propene': ('C=CC', False),
      '1,2-dichloroethene': ('ClC=CCl', True), '3-methylpent-2-ene': ('CC=C(C)CC', True),
      '2,3-dimethylbut-2-ene': ('CC(C)=C(C)C', False), 'pent-3-en-2-ol': ('CC(O)C=CC', True),
      '4-methylhex-2-ene': ('CC=CC(C)CC', True)}
for name, (smi, want) in ct.items():
    eq("cis-trans " + name, int(cis_trans_alkene(smi)), int(want))
ring = {'1,3-dimethylcyclohexane': ('CC1CCCC(C)C1', True), '1,1-dimethylcyclohexane': ('CC1(C)CCCCC1', False),
        '1,4-dimethylcyclohexane': ('CC1CCC(C)CC1', True), '1,2-dimethylcyclohexane': ('CC1CCCCC1C', True)}
for name, (smi, want) in ring.items():
    eq("ring cis-trans " + name, int(ring_cis_trans(smi)), int(want))

# ---- stereoisomer counts
eq("pent-3-en-2-ol stereoisomers", 2 ** len(chiral_centres('CC(O)C=CC')) * (2 if cis_trans_alkene('CC(O)C=CC') else 1), 4)
eq("4-methylhex-2-ene stereoisomers", 2 ** len(chiral_centres('CC=CC(C)CC')) * (2 if cis_trans_alkene('CC=CC(C)CC') else 1), 4)
eq("threonine stereoisomers", 2 ** len(chiral_centres('CC(O)C(N)C(=O)O')), 4)
eq("butan-2-ol enantiomers", 2 ** 1, 2)

# ---- butanoic acid / ethyl ethanoate (real context)
Mr = 4 * C + 8 * H + 2 * O
eq("Mr C4H8O2", Mr, 88.0)
eq("butanoic acid H", 3 + 2 + 2 + 1, 8); eq("ethyl ethanoate H", 3 + 2 + 3, 8)
eq("ethyl ethanoate C", 2 + 2, 4)
# pentane vs methylpropane etc: sigma bonds
eq("propene sigma", 9 - 1, 8)

# ---- A Level: yield from a racemic mixture
eq("racemic active mass", 6.50 * 0.50, 3.25)
eq("separation yield", sf(3.25 * 0.85), 2.76)       # 2.7625
eq("chiral catalyst mass", sf(6.50 * 0.92), 5.98)
assert 5.98 > 2 * 2.76
print("ok", n)
