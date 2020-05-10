from utils.bellman_ford import bellman_ford
from utils.dijkstra import dijkstra
from utils.representation import AdjacencyList

from math import inf
from copy import deepcopy


def johnson(g_rep, g_tup, weights, n):
    g_rep_prim, g_tup_prim, weights_prim = add_node_to_graph(g_rep, g_tup, n, weights)
    d, p, bool = bellman_ford(g_rep_prim, weights_prim, n)
    print(weights_prim)
    if not bool:
        print("G zawiera cykl o ujemnej wadze")
        exit(-1)

    h = d
    w = {(u, v): weights_prim[(u, v)] + h[u] - h[v] for (u, v) in weights_prim.keys()}

    D = [[inf for j in range(n)] for i in range(n)]

    adjList = {i: [] for i in range(n)}
    for i, j in weights.keys():
        adjList[i].append(j)
        adjList[j].append(i)

    G = AdjacencyList({'list': adjList, 'position': {}, 'colors': {}})

    for u in range(n):
        d_prim, p_prim = dijkstra(G, w, u)
        # print(f'd_prim {u}:', d_prim)
        for v in range(n):
            D[u][v] = d_prim[v] - h[u] + h[v]
    return D


def add_node_to_graph(g_rep, g_tup, n, weights):
    g_rep_prim = deepcopy(g_rep)
    g_tup_prim = deepcopy(g_tup)
    weights_prim = deepcopy(weights)
    g_rep_prim.append([])
    for i in range(n):
        g_rep_prim[i].append((n, "from", {'weight': 0}))
        g_rep_prim[n].append((i, "to", {'weight': 0}))
        g_tup_prim.append((n, i, {'weight': 0}))
        weights_prim[(n, i)] = 0

    return g_rep_prim, g_tup_prim, weights_prim
