from tasks.lab2_task1 import degree_seq, create_adjacency_list, randomize_edges

A = [4, 3, 3, 2, 2, 1, 1]
print(degree_seq(A, 7))
adjency_list = create_adjacency_list(A)
print("adjency list ", adjency_list)
A_randomized = randomize_edges(A)
print("Adjencency list after randomisation: ", A_randomized)
