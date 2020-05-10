from math import cos, sin, pi, inf
import networkx as nx
import matplotlib.pyplot as plt

from utils.bellman_ford import bellman_ford

from tasks.lab4_task1 import rand_digraph_edge_probability
from tasks.lab4_task2 import kosaraju


def generate_strongly_connected_graph(n):
    gRep, gTup = rand_digraph_edge_probability(n, 0.6)

    check = kosaraju(gRep)
    while len(set(check)) != 1:
        gRep, gTup = rand_digraph_edge_probability(n, 0.6)
        check = kosaraju(gRep)
    return gRep, gTup


def print_graph(gTup, n):
    positions = {}
    radius = 8
    alpha = 2 * pi / n

    x_0 = 20
    y_0 = 20
    for i in range(n):
        positions.update(
            {i: (x_0 + radius * cos(i * alpha), y_0 + radius * sin(i * alpha))})

    graph_p = nx.DiGraph()
    for i, item in enumerate(positions):
        graph_p.add_node(i, pos=item)
    graph_p.add_edges_from(gTup)
    labels = nx.get_edge_attributes(graph_p, 'weight')
    nx.draw(graph_p, pos=positions)
    nx.draw_networkx_labels(graph_p, pos=positions)
    nx.draw_networkx_edge_labels(graph_p, pos=positions, edge_labels=labels, font_color='red')
    plt.show()


def lab4_task3(n, start):
    gRep, gTup = generate_strongly_connected_graph(n)

    dictOfEdges = {(i, j): z['weight'] for i, j, z in gTup}  # kluczem jest krotka z krawedzia, wartoscia jest waga

    d, p, error = bellman_ford(gRep, dictOfEdges, start)
    if error:
        return gTup, d, p
    else:
        print("W grafie jest cykl o ujemnej wadze osiągalny ze źródła s")
        return gTup, d, p

