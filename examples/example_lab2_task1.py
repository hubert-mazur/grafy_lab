from tasks.lab2_task1 import degree_seq, create_adjacency_list, randomize_edges, print_graph
# A = [4, 4, 3, 1, 2]
A = [4, 3, 3, 2, 2, 1, 1]
# A = [8, 8, 8, 6, 4, 4, 4, 2, 2, 2]
# A = [4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 1]

if degree_seq(A, len(A)): 

    adjency_list = create_adjacency_list(A)
    A_randomized = randomize_edges(A)


    edges_list = [tuple(i) for i in adjency_list]
    randomized_edges_list = [tuple(i) for i in A_randomized]

    print_graph(edges_list)

    print("\nRandomized edges list")
    print(randomized_edges_list)
    print_graph(randomized_edges_list)

else: 
    print( "List is not a degree sequence")
