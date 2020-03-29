#!/usr/bin/python3.7

import math
import copy


def get_weight(weights, u, v):
    if weights.__contains__((u, v)):
        return weights[(u, v)]
    else:
        return weights[(v, u)]


def dijkstra(G, weights, node=1):
    S = []
    Q = [int(i) for i in G.nodeList.keys()]
    d = {int(i): math.inf for i in G.nodeList.keys()}
    d[node] = 0

    p = {int(i): None for i in G.nodeList.keys()}

    while len(Q) != 0:
        min_sorted = copy.deepcopy(d)
        min_sorted = {k: v for k, v in sorted(min_sorted.items(), key=lambda z: z[1])}
        for i in min_sorted:
            if i not in S:
                S.append(i)
                Q.remove(i)
                break

        u = S[-1]

        for w in G.nodeList[u]:
            if w not in Q:
                continue
            weight = get_weight(weights, w, u)
            if d[w] > d[u] + weight:
                d[w] = d[u] + weight
                p[w] = u
    return d, p
