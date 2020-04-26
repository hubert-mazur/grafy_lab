import math
import networkx as nx
import matplotlib.pyplot as plt
from utils.representation import AdjacencyList


def drawNodesOnCircle(G: 'AdjacencyList') -> 'None':
    """
        Funkcja rysujaca graf zakodowany w postaci listy sasiedztwa.
        Parametrem jest obiekt klasy 'AdjacencyList', który przechowuje informacje o wierzcholkach i ich sasiadach.
        Wierzcholki rysowane sa na okregu o prmoieniu 8.

    :param G: AdjacencyList object
    :return: None
    """

    # liczba wierzcholkow
    nodes_number = G.numberOfNodes

    radius = 8

    # kat pomiedzy odcinkami laczacymi dwa kolejne wierzcholki i srodek okregu
    alpha = 2 * math.pi / nodes_number

    # pozycja startowa
    x_0 = 20
    y_0 = 20

    positions = {}

    # obliczenie pozycji wierzcholkow
    for i in range(1, len(G.nodeList.keys()) + 1):
        G.nodeList[int(i)] = G.nodeList.pop(i)

    for i in range(nodes_number):
        positions.update(
            {(i + 1): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})

    # rysowanie wykresu
    graph = nx.from_dict_of_lists(G.nodeList)

    plt.subplot(121).axis('off')
    plt.tight_layout()
    nx.draw_networkx_nodes(graph, pos=positions)
    nx.draw_networkx_edges(graph, pos=positions)
    nx.draw_networkx_labels(graph, pos=positions)

    plt.show()
