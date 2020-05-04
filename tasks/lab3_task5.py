from copy import deepcopy
import matplotlib.pyplot as plt
import networkx as nx
import math

'''
Wiadomo, ze do drzewa T beda nalezaly wszystkie wierzcholki. Poczatkowo nie sa polaczone (naleza do
roznych drzew). Sortujemy krawedzie grafu G wedlug niemalejacych wag. Dla kazdej krawedzi (u, v)
od najmniejszej wagi: jezeli dodanie krawedzi (u, v) nie spowoduje powstania cyklu (czyli: krawedz
(u, v) laczy rozne drzewa), to dodajemy ja do T.
'''

def min_spanning_tree_Kruskal(G_list, v): #G_list[[weight,source,dest]] -> gdzie source,dest to wierzcholki krawedzi 

    MST = []
    trees = [[k] for k in range(v)]
    G_list.sort(key = lambda x: x[0])

    for edge in range(len(G_list)): 
        weight, source, destination = deepcopy(G_list[0])
        G_list.pop(0)

        for subtree in trees: 
            if source in subtree and destination in subtree:
                break
            elif source in subtree:
                MST.append([weight, source, destination]) # append edge
                for other_subtree in trees: 
                    if destination in other_subtree:
                        idx_dest = trees.index(other_subtree)

                idx_source = trees.index(subtree)
                trees[idx_source].extend(trees[idx_dest]) 
                trees[idx_dest] = []
        
                break
    return MST


def print_graph(edges_list): 

    G = nx.Graph()
    G.add_weighted_edges_from(edges_list)

    alpha = 2 * math.pi / G.number_of_nodes()
    x_0, y_0, radius = 20, 20, 8
    
    positions = {}
    for i in range(G.number_of_nodes()):
            positions.update(
                {(i): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})
    
    plt.axis('off')
    plt.tight_layout()
    graph_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_nodes(G, pos=positions)
    nx.draw_networkx_edges(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=graph_labels ) 
    plt.show() 
            
