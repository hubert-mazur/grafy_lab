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
            
