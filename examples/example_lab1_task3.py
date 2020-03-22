import networkx as nx
import matplotlib.pyplot as plt
import tasks.lab1_task3 as t3

n = 10
mylgraph, mylegdes = t3.rand_graph_edge_number(n, 44)
mypgraph, mypegdes = t3.rand_graph_edge_probability(n, 0.5)
print(mylgraph)
print(mypgraph)
graphR = nx.Graph()
graphR.add_nodes_from([i for i in range(n)])
graphR.add_edges_from(mylegdes)
plt.subplot(121)
nx.draw(graphR, with_labels=True, font_weight='bold')
graphP = nx.Graph()
graphP.add_nodes_from([i for i in range(n)])
graphP.add_edges_from(mypegdes)
plt.subplot(122)
nx.draw(graphP, with_labels=True, font_weight='bold')
plt.show()
