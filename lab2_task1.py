def degree_seq(A, n):

    A_sorted = sorted(A, reverse = True)
    print (A_sorted)
    # warunek na nieparzysta liczbe nieparzystych cyfr w A 
    if sum(1 for i in A_sorted if i%2 == 1)%2 == 1:
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

  



A = [4,3,3,2,2,1,1]
print(degree_seq(A,7))
adjency_list = create_adjacency_list(A,7)
print("adjency list ", adjency_list)

