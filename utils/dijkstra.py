#!/usr/bin/python3.7

import math
import copy


def get_weight(weights, u, v):
    if weights.__contains__((u, v)):
        return weights[(u, v)]
    else:
        return weights[(v, u)]


def dijkstra(G, weights, node=1):
    S = []  # gotowe wierzcholki
    Q = [int(i) for i in G.nodeList.keys()]  # wszystkie wierzcholki
    d = {int(i): math.inf for i in G.nodeList.keys()}  # odleglosci od wierzcholka startowego do pozostalych
    d[node] = 0

    p = {int(i): None for i in G.nodeList.keys()}  # slownik poprzednikow wierzcholka

    while len(Q) != 0:  # iteracja do momentu, gdy wszystkie wierzcholki zostana przeniesione do S
        min_sorted = copy.deepcopy(d)
        min_sorted = {k: v for k, v in sorted(min_sorted.items(), key=lambda z: z[
            1])}  # sortowanie, w celu znalezienia wierzcholka, z najmniejszym atrybutem d
        for i in min_sorted:
            if i not in S:
                S.append(i)
                Q.remove(i)
                break

        u = S[-1]

        for w in G.nodeList[u]:  # sasiedzi wierzcholka u
            if w not in Q:  # relaksacja wierzcholkow nie nalezacych do S
                continue
            weight = get_weight(weights, w, u)
            if d[w] > d[u] + weight:
                d[w] = d[u] + weight
                p[w] = u
    return d, p


def findPath(ret, destination):
    # print(ret[1])
    # print((startNode, postNode))
    routeList = []

    elem = destination
    while elem is not None:
        routeList.append(elem)
        elem = ret[elem]
    # print(routeList)
    return routeList
