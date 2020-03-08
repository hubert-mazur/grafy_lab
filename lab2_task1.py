import random 
from copy import deepcopy 

'''
    Funkcja degree_seq- sprawdza czy lista stopni wierzcholkow grafu (lista ilosci krawedzi 
    wychodzacych z poszczegolnych wierzcholkow) jest ciagiem graficznym , zwraca True/False
'''
def degree_seq(A, n):

    A_sorted = sorted(A, reverse = True)
    print (A_sorted)
    # warunek na nieparzysta liczbe nieparzystych cyfr w A 
    if sum(i%2 for i in A_sorted)%2:
        return false 
    while True:
        if max(A_sorted) == min(A_sorted) == 0: 
            return True 
        elif A_sorted[0] < 0 or A_sorted[0] >= n or max(A_sorted) < 0:
            return False 

        for i in range(1, A_sorted[0]):
            A_sorted[i] = A_sorted[i] - 1

        A_sorted[0] = 0 
        A_sorted = sorted(A_sorted, reverse = True)


'''
    Funkcja tworzaca liste sasiedztwa na podstawie wczytanego ciagu graficznego
    zwraca liste list, podlisty zawieraja pary wierzcholkow polaczonych krawedzia 
    bez powtorzen tz krawedz [1,3] jest tozsama z [3,1]
'''
def create_adjacency_list (A, n): 
 
    edges = int(sum(A)/2) 
    A = sorted(A, reverse = True)

    #stworz liste list, podlista zawiera: nr wierzcholka, stopien wierzcholka, 
    #licznik odnotowanych polaczen (krawedzi) z danego wierzcholka
    nodes_status = [[node_idx, grade, 0] for node_idx, grade in enumerate(A) ]
    print(nodes_status)
 
    adjacency_list = set() 

    for i in range(edges):

    #usun wszyskie wierzcholki z listy dla ktorych ilosc polaczen z wierzcholka 
    #(grades) rowna jest licznikowi wykorzystanych polaczen 
        for node in nodes_status:  
            if node[1] == node[2]:
                nodes_status.remove(node)

        for node in nodes_status[1:]:
            #set zawierajacy numer wierzcholka pierwszego z nodes_status i numer kolejnego wierzcholka z nodes_status
            tmp_set = set([nodes_status[0][0], node[0]])
    
            if tmp_set not in adjacency_list:
                adjacency_list.add(frozenset(tmp_set))
                nodes_status[0][2] += 1
                node[2] += 1
                break

        nodes_status.sort(key=lambda x: x[1] - x[2], reverse=True) #posortuj po liczbie dostepnych krawedzi
  
    result_list = [list(f_set) for f_set in adjacency_list]
    result_list.sort()

    return result_list


"""
    wylosuj dwie krawedzie z list_of_edges, sprobuj je zamienic ze soba (pomieszac ich wierzcholki), 
    sprawdz czy takie krawedzie  nie wystepuja w secie pierwotnym - jesli nie - 
    zapisz zamienione krawedzie do tablicy wynikowej,- jesli tak - wylosuj ponownie krawedzie do randomizacji
"""
def randomize_edges(A, n):

    list_of_edges = create_adjacency_list(A,n)
    edges_copy = deepcopy(list_of_edges) 

    print("Adjencency list before randomisation: ", list_of_edges)
    while True: 
        first_edge, second_edge  = random.sample(edges_copy, 2)

        new_first_edge, new_second_edge = (first_edge[0], second_edge[1]), (second_edge[0], first_edge[1])

        if not(new_first_edge[0] == new_first_edge[1] or new_second_edge[0] == new_second_edge[1]):
           
            new_first_edge, new_second_edge = set(new_first_edge), set(new_second_edge)
      
            set_of_edges = set(frozenset(f_set) for f_set in list_of_edges) 
            if new_first_edge  not in set_of_edges and new_second_edge not in set_of_edges:  
                edges_copy.remove(first_edge)
                edges_copy.remove(second_edge)

                edges_copy.append(list(new_first_edge))
                edges_copy.append(list(new_second_edge))

                break

    return edges_copy

  

A = [4,3,3,2,2,1,1]
print(degree_seq(A,7))
adjency_list = create_adjacency_list(A,7)
print("adjency list ", adjency_list)
A_randomized = randomize_edges(A,7)
print("Adjencency list after randomisation: ", A_randomized)
