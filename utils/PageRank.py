import numpy as np
import random


def page_rank_random(di_graph, n, d=0.15):
    vertices = get_vertices(di_graph)
    ranks = {i: 0 for i in vertices}
    v = random.choice(vertices)
    for i in range(n):
        d = random.uniform(0, 1)
        ranks[v] += 1
        if d < 0.85:
            v = random.choice(get_neighbours(di_graph, v))
        else:
            v = random.choice(vertices)
    return {key: value / n for key, value in ranks.items()}


def get_neighbours(graph, v):
    neighbour = []
    for (u, w) in graph:
        if u == v:
            neighbour.append(w)
    return neighbour


def get_vertices(graph):
    vertices = []
    for (u, v) in graph:
        if u not in vertices:
            vertices.append(u)
    return vertices


def page_rank_vector(graph, n_iterations, d=0.15):
    n = len(graph[0])
    p = np.array([1 / n for i in graph])
    P = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            P[i].append((1 - d) * (graph[i][j] / sum(graph[i])) + d / n)

    P = np.array(P)

    for l in range(n_iterations):
        p = p @ P

    return {i : p[i] for i in range(len(p))}


