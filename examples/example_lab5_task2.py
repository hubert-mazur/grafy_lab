from tasks.lab5_task2 import BSF, FordFulkerson, print_graph
import networkx as nx

# list_of_edges = [(0,1,10),(0,2,9),(1,2,6),(1,3,5),(2,4,8),(4,1,4),(4,3,2),(4,5,7),(3,5,9)]
list_of_edges = [(0, 1, 9), (0, 2,12), (1, 2, 6), (1, 5, 3),
                 (1, 4, 4), (1, 3, 9), (2, 3, 2), (2, 4, 6), 
                 (2, 5, 3), (3, 4, 2), (3, 6, 7), (4, 6, 8),
                 (4, 5, 2), (5, 6, 5)]

G = nx.DiGraph()
G.add_weighted_edges_from(list_of_edges)
source, dest = 0, 6
        
max_flow, list_flow = FordFulkerson(G, source, dest)
print("Max flow ", max_flow)
print_graph(G, list_flow)