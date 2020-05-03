from copy import deepcopy

def kosaraju(GRep):
    G = [i for i, u in enumerate(GRep)]
    d = [-1 for _ in G]
    f = [-1 for _ in G]
    t = 0
    for v in G:
        if d[v] == -1:
            dfs_visit(v, GRep, d, f, t)
    GTRep = transpose_graph(GRep)
    nr = 0
    comp = [-1 for _ in G]
    f.sort(key=lambda x: x, reverse=True)
    G = [x for _, x in sorted(zip(f, G))]
    for v in G: # w kolejności malejących czasów f[v]
        if comp[v] == -1:
            nr = nr + 1
        comp[v] = nr
        components_r(nr, v, GTRep, comp)
    return comp

def dfs_visit(v, GRep, d, f, t):
    t = t + 1
    d[v] = t
    tempG = [i for i, l, w in GRep[v] if l == 'to']
    for u in tempG: #Przejście po krawędzi (v, u)
        if d[v] == -1:
            dfs_visit(u, GRep, d, f, t)
    t = t + 1
    f[v] = t #W implementacji ze stosem: tutaj należy dodać v do stosu.

def components_r(nr, v, GT, comp):
    print()
    tempG = [i for i, l, w in GT[v] if l == 'to']
    for u in tempG:
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, GT, comp)

def transpose_graph(G):
    GT = deepcopy(G)
    for v in GT:
        for i, e in enumerate(v):
            if e[1] == 'to':
                v[i] = (e[0], 'from', e[2])
            else:
                v[i] = (e[0], 'to', e[2])
    return GT
