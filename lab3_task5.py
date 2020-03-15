from copy import deepcopy

'''
Wiadomo, że do drzewa T będą należały wszystkie wierzchołki. Początkowo nie są połączone (należą do
różnych drzew). Sortujemy krawędzie grafu G według niemalejących wag. Dla każdej krawędzi (u, v)
od najmniejszej wagi: jeżeli dodanie krawędzi (u, v) nie spowoduje powstania cyklu (czyli: krawędź
(u, v) łączy różne drzewa), to dodajemy ją do T.

'''

def min_spanning_tree_Kruskal(G_list, v): #G_list[[weight,source,dest]] -> gdzie source,dest to wierzcholki krawedzi 

    MST = []
    trees = [[k] for k in range(v)]
    G_list.sort(key = lambda x: x[0])

    for node in range(len(G_list)): 
        weight, source, destination = deepcopy(G_list[0])
        print("Handling edge from {} to {} with weight {}".format(source, destination, weight))
        G_list.pop(0)

        for subtree in trees: 
            if source in subtree and destination in subtree:
                print("{} and {} already in {}".format(source, destination, subtree))
                continue
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
            
    
   
list_of_values = [[7,2,3],[7,7,8],[8,0,7],[8,1,2],[9,3,4],[10,5,4],[11,1,7],[14,3,5],[1,7,6],[2,8,2],[2,6,5],[4,0,1],[4,2,5],[6,8,6]]
mst = min_spanning_tree_Kruskal(list_of_values, 9)

print("Printing spanning tree")
for weight, source, destination in sorted(mst, key=lambda edge: edge[1]):
    print("Edge from {} to {} (weight: {})".format(source, destination, weight))


