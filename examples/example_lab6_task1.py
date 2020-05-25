from utils.PageRank import page_rank_random, page_rank_vector
import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy as np


def task1():
    # di_graph = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 4), (8, 5))
    di_graph = ((0, 1), (0, 3), (0, 4),
                (1, 4), (1, 2),
                (2, 1), (2, 3), (2, 5),
                (3, 1),
                (4, 1), (4, 3), (4, 5),
                (5, 1))
    ranks = page_rank_random(di_graph, 100000)

    print(sorted(ranks.items(), key=lambda x: x[1], reverse=True))

    graph = nx.DiGraph()
    graph.add_edges_from(di_graph)

    radius = 8
    nodes = len(graph)
    alpha = 2 * math.pi / nodes

    x_0, y_0 = 20, 20
    positions = {}

    for i in range(nodes):
        positions.update(
            {(i): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})

    nx.draw_networkx_labels(graph, pos=positions)
    nx.draw(graph, pos=positions)
    plt.show()


def task2():

    di_graph = np.array([[0., 1, 0, 1, 1, 0],
                         [0, 0, 1, 0, 1, 0],
                         [0, 1, 0, 1, 0, 1],
                         [0, 1, 0, 0, 0, 0],
                         [0, 1, 0, 1, 0, 1],
                         [0, 1, 0, 0, 0, 0]
                         ])

    ranks = page_rank_vector(di_graph, 100)

    print(sorted(ranks.items(), key=lambda x: x[1], reverse=True))

    graph = nx.from_numpy_array(di_graph)

    radius = 8
    nodes = len(graph)
    alpha = 2 * math.pi / nodes

    x_0, y_0 = 20, 20
    positions = {}

    for i in range(nodes):
        positions.update(
            {(i): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})

    nx.draw_networkx_labels(graph, pos=positions)
    nx.draw(graph, pos=positions)
    plt.show()


task1()
task2()