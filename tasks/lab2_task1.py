import random
from copy import deepcopy
import matplotlib.pyplot as plt
import networkx as nx
import math
import random

def degree_seq(A, n):
    '''
        Funkcja degree_seq- sprawdza czy lista stopni wierzcholkow grafu (lista ilosci krawedzi
        wychodzacych z poszczegolnych wierzcholkow) jest ciagiem graficznym , zwraca True/False
    '''
    A_sorted = sorted(A, reverse = True)
    # warunek na nieparzysta liczbe nieparzystych cyfr w A 
    if sum(i%2 for i in A_sorted)%2:
        return False 
    
    while True:
        if max(A_sorted) == min(A_sorted) == 0: 
            return True 
        elif A_sorted[0] < 0 or A_sorted[0] >= n or max(A_sorted) < 0:
            return False
        else:   

            for i in range(1, A_sorted[0] + 1):
                if A_sorted[i] >= 1:
                    A_sorted[i] = A_sorted[i] - 1
                else:
                    return False

            A_sorted[0] = 0 
            A_sorted = sorted(A_sorted, reverse = True)
            

def create_adjacency_list(A):
    '''
        Funkcja tworzaca liste sasiedztwa na podstawie wczytanego ciagu graficznego
        zwraca liste list, podlisty zawieraja pary wierzcholkow polaczonych krawedzia
        bez powtorzen tz krawedz [1,3] jest tozsama z [3,1].
        Zawiera sortowanie dobieranych wezlow po ilosci dostepnych slotow, 
        minimalizuje szane ze niemoznaby znalezc wezla, z ktorym moznaby polaczyc aktualny wezel 
    '''
    edges = int(sum(A)/2) 
    A = sorted(A, reverse = True)

    #stworz liste list, podlista zawiera: nr wierzcholka, stopien wierzcholka, 
    #licznik odnotowanych polaczen (krawedzi) z danego wierzcholka
    nodes_status = [[node_idx, grade, 0] for node_idx, grade in enumerate(A) ]
    adjacency_list = set()

    # na wszelki wypadek sortuje liste malejaco po ilosci dostepnych slotow
    nodes_status = sorted(nodes_status, key=lambda x: x[1], reverse=True)
    for i in range(edges):
    #zostaw w liscie wierzcholki, z ktorych mozna wyprowadzic przynajmniej jedna krawedz 
        nodes_status = [node for node in nodes_status if int(node[1]) > int(node[2])]

        for node in sorted(nodes_status[1:], key=lambda x: (x[1] - x[2], x[1]), reverse=True):
            #set zawierajacy numer wierzcholka pierwszego z nodes_status i numer kolejnego wierzcholka z nodes_status
            maybe_edge = set([nodes_status[0][0], node[0]])
    
            if maybe_edge not in adjacency_list:
                adjacency_list.add(frozenset(maybe_edge))
                nodes_status[0][2] += 1
                node[2] += 1
                break
  
    result_list = [list(f_set) for f_set in adjacency_list]
    result_list.sort(key=lambda x: (x[0], x[1]))

    return result_list


def randomize_edges(A):
    '''
        wylosuj dwie krawedzie z list_of_edges, sprobuj je zamienic ze soba (pomieszac ich wierzcholki),
        sprawdz czy takie krawedzie  nie wystepuja w liscie pierwotnej - jesli nie -
        zapisz zamienione krawedzie do listy wynikowej,- jesli tak - wylosuj ponownie krawedzie do randomizacji
    '''
    list_of_edges = create_adjacency_list(A)
    edges_copy = deepcopy(list_of_edges)
 
    while True:
        first_edge, second_edge = random.sample(edges_copy, 2)
        new_first_edge, new_second_edge = [first_edge[0], second_edge[1]], [second_edge[0], first_edge[1]] 

        if not(new_first_edge[0] == new_first_edge[1] or new_second_edge[0] == new_second_edge[1]):

            if (new_first_edge not in list_of_edges and new_first_edge[::-1] not in list_of_edges) and  \
                (new_second_edge not in list_of_edges  and new_second_edge[::-1] not in list_of_edges):

                edges_copy.remove(first_edge)
                edges_copy.remove(second_edge)

                edges_copy.append(new_first_edge)
                edges_copy.append(new_second_edge)

                # print("\nRandomized edges")
                # print(first_edge, second_edge)
                # print(new_first_edge, new_second_edge)

                break

    return edges_copy


def print_graph(edges_list): 

    G = nx.Graph()
    G.add_edges_from(edges_list)

    radius = 8
    alpha = 2 * math.pi / G.number_of_nodes()

    x_0 = 20
    y_0 = 20

    positions = {}
    for i in range(G.number_of_nodes()):
            positions.update(
                {(i): (x_0 + radius * math.cos(i * alpha), y_0 + radius * math.sin(i * alpha))})
    

    plt.axis('off')
    plt.tight_layout()
    nx.draw_networkx_nodes(G, pos=positions)
    nx.draw_networkx_edges(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions)

    
    # plt.savefig("graph.png") # save as png
    plt.show() 
