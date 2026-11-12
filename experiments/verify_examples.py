"""Sanity checks for the worked examples and elementary lemmas in
reports/fuzzy-soft-graphs-research-roadmap.md.

A fuzzy soft graph (FSG) is stored as {parameter: {frozenset({u, v}): mu}};
vertex memberships are taken to be 1 (enough for every example used here).
Run:  python3 experiments/verify_examples.py
"""
from itertools import combinations, product
import random

import numpy as np


def conn(n, mu, skip=None):
    """All-pairs strength of connectedness (max-min closure, Floyd-Warshall)."""
    c = [[0.0] * n for _ in range(n)]
    for e, w in mu.items():
        if e == skip:
            continue
        u, v = tuple(e)
        c[u][v] = c[v][u] = max(c[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = max(c[i][j], min(c[i][k], c[k][j]))
    return c


def strong_arcs(n, mu):
    """Arcs with mu(xy) >= CONN_{G-xy}(x, y) (Bhutani-Rosenfeld strong arcs)."""
    out = set()
    for e, w in mu.items():
        if w <= 0:
            continue
        u, v = tuple(e)
        if w >= conn(n, mu, skip=e)[u][v]:
            out.add(e)
    return out


def meet(layers):
    keys = set().union(*[set(m) for m in layers.values()])
    return {e: min(m.get(e, 0.0) for m in layers.values()) for e in keys}


def gap(n, layers):
    """Consensus gap: min_e CONN_e(x,y) - CONN_meet(x,y) for every pair."""
    cs = [conn(n, m) for m in layers.values()]
    cm = conn(n, meet(layers))
    return {(x, y): min(c[x][y] for c in cs) - cm[x][y]
            for x, y in combinations(range(n), 2)}


def dominates(n, edges, D):
    return all(v in D or any(frozenset((v, d)) in edges for d in D) for v in range(n))


def sim_domination(n, edge_sets, independent=False):
    """Smallest D dominating every layer (optionally independent in the union)."""
    union = set().union(*edge_sets)
    for k in range(1, n + 1):
        for D in combinations(range(n), k):
            if independent and any(frozenset(p) in union for p in combinations(D, 2)):
                continue
            if all(dominates(n, E, set(D)) for E in edge_sets):
                return k, D
    return None


def energy(n, mu):
    A = np.zeros((n, n))
    for e, w in mu.items():
        u, v = tuple(e)
        A[u, v] = A[v, u] = w
    return float(np.abs(np.linalg.eigvalsh(A)).sum()), A


def lam2(n, mu):
    _, A = energy(n, mu)
    return float(np.sort(np.linalg.eigvalsh(np.diag(A.sum(1)) - A))[1])


E = lambda *pairs: {frozenset(p) for p in pairs}
close = lambda a, b: abs(a - b) < 1e-9

# 1. Consensus gap can be positive: 4-cycle a-b-c-d (Example 6.1).
C4 = {1: {frozenset((0, 1)): 1, frozenset((1, 2)): 1, frozenset((2, 3)): 1, frozenset((3, 0)): .5},
      2: {frozenset((0, 1)): .5, frozenset((1, 2)): 1, frozenset((2, 3)): 1, frozenset((3, 0)): 1}}
assert close(gap(4, C4)[(0, 1)], 0.5)

# 2. Zero gap does NOT force a common maximum spanning tree (Example 6.2).
T = {1: {frozenset((0, 1)): 1, frozenset((1, 2)): .9, frozenset((0, 2)): .8},
     2: {frozenset((0, 1)): .1, frozenset((1, 2)): .2, frozenset((0, 2)): .3}}
assert all(close(g, 0) for g in gap(3, T).values())
assert strong_arcs(3, T[1]) == E((0, 1), (1, 2)) and strong_arcs(3, T[2]) == E((1, 2), (0, 2))

# 3. Gap ~ 1 on every pair with three layers on a triangle (Remark 6.4).
eps = 0.01
tri = {i: {frozenset(p): (eps if j == i else 1.0)
           for j, p in enumerate([(0, 1), (1, 2), (0, 2)])} for i in range(3)}
assert all(close(g, 1 - eps) for g in gap(3, tri).values())

# 4. Realisability lemma (Lemma 2.1): random connected spanning S of random G*.
random.seed(1)
for _ in range(300):
    n = random.randint(3, 7)
    tree = [frozenset((i, random.randrange(i))) for i in range(1, n)]
    extra = [frozenset(p) for p in combinations(range(n), 2) if random.random() < .5]
    S = set(tree) | {e for e in extra if random.random() < .4}
    G = S | set(extra)
    mu = {e: (1.0 if e in S else 0.5) for e in G}
    assert strong_arcs(n, mu) == S

# 5. Simultaneous independent dominating sets need not exist (Example 3.1).
L1, L2 = E((0, 1), (1, 2)), E((0, 1), (0, 2))
assert sim_domination(3, [L1, L2], independent=True) is None
assert sim_domination(3, [L1, L2])[0] == 2

# 6. Elementary bounds max_e gamma <= gamma_sim <= sum_e gamma on random layers.
for _ in range(200):
    n = random.randint(3, 7)
    layers = []
    for _ in range(random.randint(2, 3)):
        tree = {frozenset((i, random.randrange(i))) for i in range(1, n)}
        layers.append(tree | {frozenset(p) for p in combinations(range(n), 2) if random.random() < .2})
    gs = [sim_domination(n, [L])[0] for L in layers]
    g = sim_domination(n, layers)[0]
    assert max(gs) <= g <= min(sum(gs), n)

# 7. Energy: strict subadditivity (P3 = two edge-disjoint K2 layers) and bounds.
e1, _ = energy(3, {frozenset((0, 1)): 1.0})
e2, _ = energy(3, {frozenset((1, 2)): 1.0})
e12, _ = energy(3, {frozenset((0, 1)): 1.0, frozenset((1, 2)): 1.0})
assert close(e12, 2 * 2 ** .5) and e12 < e1 + e2
for _ in range(300):
    n = random.randint(3, 8)
    ms = [{frozenset(p): random.random() for p in combinations(range(n), 2)} for _ in range(3)]
    w = np.random.dirichlet(np.ones(3))
    mix = {e: sum(w[i] * ms[i][e] for i in range(3)) for e in ms[0]}
    assert energy(n, mix)[0] <= sum(w[i] * energy(n, ms[i])[0] for i in range(3)) + 1e-9
    assert lam2(n, mix) >= sum(w[i] * lam2(n, ms[i]) for i in range(3)) - 1e-9
    s2 = sum(v * v for v in ms[0].values())
    en = energy(n, ms[0])[0]
    assert 2 * s2 ** .5 - 1e-9 <= en <= (2 * n * s2) ** .5 + 1e-9

# 8. Mixing layers can beat every single layer in algebraic connectivity.
a, b = {frozenset((0, 1)): 1.0}, {frozenset((1, 2)): 1.0}
half = {frozenset((0, 1)): .5, frozenset((1, 2)): .5}
assert close(lam2(3, a), 0) and close(lam2(3, b), 0) and close(lam2(3, half), .5)

# 9. Bottleneck objectives commute with the meet (Theorem 9.1), brute force.
def paths(n, s, t):
    for k in range(n - 1):
        for mid in map(list, __import__("itertools").permutations([v for v in range(n) if v not in (s, t)], k)):
            yield [s] + mid + [t]
for _ in range(100):
    n = 5
    ms = {i: {frozenset(p): random.random() for p in combinations(range(n), 2)} for i in range(3)}
    best = max(min(min(m[frozenset(q)] for q in zip(P, P[1:])) for m in ms.values()) for P in paths(n, 0, 4))
    assert close(best, conn(n, meet(ms))[0][4])

# 10. Remark 2.3: distinct weights => strong-arc graph is the max spanning tree.
for _ in range(200):
    n = random.randint(3, 7)
    mu = {frozenset(p): random.random() for p in combinations(range(n), 2)}
    comp, mst = list(range(n)), set()
    find = lambda v: v if comp[v] == v else find(comp[v])
    for e in sorted(mu, key=mu.get, reverse=True):
        u, v = tuple(e)
        if find(u) != find(v):
            comp[find(u)] = find(v)
            mst.add(e)
    assert strong_arcs(n, mu) == mst

# 11. tau(C_n) = n: fewest spanning trees of a cycle with empty intersection.
for n in range(3, 7):
    cyc = [frozenset((i, (i + 1) % n)) for i in range(n)]
    trees = [set(cyc) - {f} for f in cyc]
    tau = next(k for k in range(1, n + 1)
               if any(not set.intersection(*c) for c in combinations(trees, k)))
    assert tau == n

# 12. Commuting layers with positive energy deficit: two matchings of C4.
m1 = {frozenset((0, 1)): 1.0, frozenset((2, 3)): 1.0}
m2 = {frozenset((1, 2)): 1.0, frozenset((3, 0)): 1.0}
(ea, Aa), (eb, Ab) = energy(4, m1), energy(4, m2)
assert np.allclose(Aa @ Ab, Ab @ Aa) and close(ea, 4) and close(eb, 4)
assert close(energy(4, {e: .5 for e in list(m1) + list(m2)})[0], 2)

print("all checks passed")
