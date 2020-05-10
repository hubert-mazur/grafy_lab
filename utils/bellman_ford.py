from math import inf

from utils.dijkstra import get_weight


def bellman_ford(g_rep, weights, start):
    n = len(g_rep)
    G = [i for i, u in enumerate(g_rep)]
    # d = [inf if i != start else 0 for i in G]

    d = {int(i): inf for i in G}  # odleglosci od wierzcholka startowego do pozostalych
    d[start] = 0
    p = {int(i): None for i in G}  # slownik poprzednikow wierzcholka

    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            p[v] = u

    for i in range(1, n - 1):
        for u, v in weights.keys():
            relax(u, v, get_weight(weights, u, v))

    for u, v in weights.keys():
        if d[v] > d[u] + get_weight(weights, u, v):
            return 0, 0, False

    return d, p, True
